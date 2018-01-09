# -*- coding: utf-8 -*

import numpy as np
import pandas as pd
import xgboost as xgb
import utils as utils

from xgboost.sklearn import XGBClassifier
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV

import matplotlib.pylab as plt
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4


basedir = utils.findPath()

continent_gdp = pd.read_csv(basedir + "continent.csv")

# orderHistory和userComment结合，并生成特征
def createFeature(dataset):
    orderHistory = pd.read_csv(basedir + "orderHistory_" + dataset + ".csv")
    userComment = pd.read_csv(basedir + "userComment_" + dataset + ".csv")
    orderFuture = pd.read_csv(basedir + "orderFuture_" + dataset + ".csv")
    userOrderHistoryComment = pd.merge(orderHistory, userComment, on=["userid", "orderid"], how='left')
    userOrderHistoryComment = pd.merge(userOrderHistoryComment, continent_gdp, on=["continent", ], how='left')
    print userOrderHistoryComment.head(1)
    userOrderHistoryComment.drop('commentsKeyWords', axis=1, inplace=True)
    userOrderHistoryComment.drop('orderid', axis=1, inplace=True)

    userOrderHistoryComment_group = userOrderHistoryComment.groupby('userid')

    orderDf = pd.DataFrame(orderFuture['userid'], columns=['userid'])

    orderDf = orderDf.join(userOrderHistoryComment_group['orderType'].count(), on='userid')
    orderDf.rename(columns={'orderType': 'order_num'}, inplace=True)

    orderDf = orderDf.join(userOrderHistoryComment_group['rating'].mean(), on='userid')
    orderDf.rename(columns={'rating': 'rating_mean'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['rating'].max(), on='userid')
    orderDf.rename(columns={'rating': 'rating_max'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['rating'].min(), on='userid')
    orderDf.rename(columns={'rating': 'rating_min'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['rating'].std(), on='userid')
    orderDf.rename(columns={'rating': 'rating_std'}, inplace=True)

    # Order Time
    orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].mean(), on='userid')
    orderDf.rename(columns={'orderTime': 'orderTime_mean'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].median(), on='userid')
    orderDf.rename(columns={'orderTime': 'orderTime_median'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].min(), on='userid')
    orderDf.rename(columns={'orderTime': 'orderTime_min'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].std(), on='userid')
    orderDf.rename(columns={'orderTime': 'orderTime_std'}, inplace=True)

    orderDf = orderDf.join(userOrderHistoryComment_group['orderType'].sum(), on='userid')
    orderDf.rename(columns={'orderType': 'orderType_sum'}, inplace=True)

    orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].mean(), on='userid')
    orderDf.rename(columns={'continent_gdp': 'continent_gdp_mean'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].max(), on='userid')
    orderDf.rename(columns={'continent_gdp': 'continent_gdp_max'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].min(), on='userid')
    orderDf.rename(columns={'continent_gdp': 'continent_gdp_min'}, inplace=True)
    orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].std(), on='userid')
    orderDf.rename(columns={'continent_gdp': 'continent_gdp_std'}, inplace=True)

    order_month = pd.read_csv(basedir + "order_month_" + dataset + ".csv")
    orderDf = pd.merge(orderDf, order_month, on=["userid"], how='left')
    return orderDf

# 处理userProfile, 生成特征
city_data = pd.read_csv(basedir + "city_info.data", delimiter='\t', names = ['province', 'city_gdp', 'city_gdp1'])
city_data.drop('city_gdp1', axis=1, inplace=True)
def createUserProfileFeature(dataset):
    userProfile = pd.read_csv(basedir + "userProfile_" + dataset + ".csv")
    userProfile_deal = pd.merge(userProfile, city_data, on=['province'], how='left')
    userProfile_deal.drop('province', axis=1, inplace=True)
    print userProfile_deal.dtypes
    userProfile_deal['age'].fillna("null", inplace=True)

    def convertAge(x):
        if x == 'null':
            return 0
        x = str(x)
        num = int(x.split('后')[0])
        if(num == 0):
             return 18
        else:
            return 2018 - 1900 - num

    userProfile_deal['age'] = userProfile_deal['age'].apply(lambda x: convertAge(x))
    return userProfile_deal

# 关于actionTime生成特征
def createActionTimeFeature(dataset):
    action_dataset = pd.read_csv(basedir + "action_" + dataset + ".csv")
    orderFuture = pd.read_csv(basedir + "orderFuture_" + dataset + ".csv")

    action_train_group = action_dataset.groupby('userid')
    actionDf = pd.DataFrame(orderFuture['userid'], columns=['userid'])

    actionDf = actionDf.join(action_train_group['actionTime'].mean(), on='userid')
    actionDf.rename(columns={'actionTime': 'actionTime_mean'}, inplace=True)
    actionDf = actionDf.join(action_train_group['actionTime'].max(), on='userid')
    actionDf.rename(columns={'actionTime': 'actionTime_max'}, inplace=True)
    actionDf = actionDf.join(action_train_group['actionTime'].min(), on='userid')
    actionDf.rename(columns={'actionTime': 'actionTime_min'}, inplace=True)
    actionDf = actionDf.join(action_train_group['actionTime'].std(), on='userid')
    actionDf.rename(columns={'actionTime': 'actionTime_std'}, inplace=True)
    return actionDf

# 生成总的特征数据
def createTotalFeatures(dataset):
    action_type_rate = pd.read_csv(basedir + "action_rate_" + dataset + ".csv")
    user_month_action = pd.read_csv(basedir + "user_month_" + dataset + ".csv")
    orderFuture_train = pd.read_csv(basedir + "orderFuture_train.csv")
    orderDf = createFeature(dataset)
    actionDf = createActionTimeFeature(dataset)
    userProfile_deal = createUserProfileFeature(dataset)

    action_result = pd.merge(user_month_action, action_type_rate, on=["userid"], how='left')
    print action_result.shape
    train_data = pd.merge(orderDf, action_result, on=['userid'], how='left')
    train_data = pd.merge(train_data, actionDf, on=['userid'], how='left')
    train_data = pd.merge(userProfile_deal, train_data, on=['userid'], how='left')
    if dataset == 'train':
        train_data = pd.merge(orderFuture_train, train_data, on=['userid'], how='left')
        train_data.rename(columns={'orderType': 'label'}, inplace=True)

    action_interval_train = pd.read_csv(basedir + "action_interval_" + dataset + ".csv")
    train_data = pd.merge(train_data, action_interval_train, on=['userid'], how='left')

    # One-Hot Coding
    train_data = pd.get_dummies(train_data, columns=['gender'], dummy_na=True)
    return train_data


def modelfit(alg, dtrain, dtest, predictors, useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(dtrain[predictors].values, label=dtrain[target].values)
        xgtest = xgb.DMatrix(dtest[predictors].values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                          metrics='auc', early_stopping_rounds=early_stopping_rounds)
        print cvresult.shape[0]
        alg.set_params(n_estimators=cvresult.shape[0])

    # Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain['label'], eval_metric='auc')

    # Predict training set:
    dtrain_predictions = alg.predict(dtrain[predictors])
    dtrain_predprob = alg.predict_proba(dtrain[predictors])[:, 1]

    # Print model report:
    print "\nModel Report"
    print "Accuracy : %.4g" % metrics.accuracy_score(dtrain['label'].values, dtrain_predictions)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(dtrain['label'], dtrain_predprob)

    feat_imp = pd.Series(alg.booster().get_fscore()).sort_values(ascending=False)
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')


target='label'
IDcol = 'userid'

train_data = createTotalFeatures('train')
test_data = createTotalFeatures('test')

predictors = [x for x in train_data.columns if x not in [target, IDcol]]
xgb1 = XGBClassifier(
        learning_rate =0.1,
        n_estimators=1000,
        max_depth=5,
        min_child_weight=1,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective= 'binary:logistic',
        nthread=4,
        scale_pos_weight=1,
        seed=27)
modelfit(xgb1, train_data, test_data, predictors)

# 生成提交文件
prob = xgb1.predict_proba(test_data[predictors])[:,1]
submit = pd.read_csv(basedir + "orderFuture_test.csv")
submit['orderType'] = prob
submit.to_csv(basedir + "submit_c.csv", index = False)