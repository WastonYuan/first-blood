
import numpy as np
import xgboost as xgb

data1 = np.loadtxt('data/neuro_feat.tsv', delimiter='\t')
data2 = np.loadtxt('data/train_data.tsv', delimiter='\t')
data3 = np.loadtxt('data/country_feat.tsv', delimiter='\t')

data = np.array([np.concatenate((data2[i][:], data3[i][1:], data1[i][1:])) for i in range(data1.__len__())])
data = np.array([np.concatenate((data2[i][:], data3[i][1:])) for i in range(data1.__len__())])
data = data2

#build param
train_x = data[:int(data.shape[0]*0.7),1:]
train_y = data[:int(data.shape[0]*0.7),0]
test_x = data[int(data.shape[0]*0.7):,1:]
test_y = data[int(data.shape[0]*0.7):,0]
dtrain = xgb.DMatrix(train_x, label=train_y)
dtest = xgb.DMatrix(test_x, label=test_y)

#tuning start
params = {'gamma':2.0,'nthread':8, 'max_depth':5, 'eta':0.1, 'silent':1, 'objective':'binary:logistic', 'eval_metric':'auc'}

watchlist = [(dtrain,'train'), (dtest,'eval')]

num_round = 600
bst = xgb.train(params, dtrain, num_round, watchlist, early_stopping_rounds=50)
#tuning end
# bst.predict(dtrain)

#make xgboost
save_train_x = data[:,1:]
save_train_y = data[:,0]
save_dtrain = xgb.DMatrix(save_train_x, label=save_train_y)
save_bst = xgb.train(params, save_dtrain, num_round, watchlist, early_stopping_rounds=50)

save_bst.save_model('xgb_model/xgb_v3.model')