from sklearn.datasets import load_iris
import numpy as np

data = np.loadtxt('data/neuro_feat.tsv', delimiter='\t')

train_x = data[:int(data.shape[0]*0.7),1:]
train_y = data[:int(data.shape[0]*0.7),0]
test_x = data[int(data.shape[0]*0.7):,1:]
test_y = data[int(data.shape[0]*0.7):,0]



#########lr
from sklearn.datasets import load_iris

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression(verbose=True)
logistic.fit(train_x,train_y)
print 'Predicted class %s, real class %s' % ( logistic.predict(test_x),test_y)
print 'Probabilities for each class: %s' % logistic.predict_proba(train_x), test_y


###########xgb
import xgboost as xgb
import os


dtrain = xgb.DMatrix(train_x, label=train_y)
dtest = xgb.DMatrix(test_x, label=test_y)

params = {'gamma':2.0,'nthread':8, 'max_depth':15, 'eta':0.3, 'silent':1, 'objective':'binary:logistic', 'eval_metric':'auc'}

watchlist = [(dtrain,'train'), (dtest,'eval')]


num_round = 50
bst = xgb.train(params, dtrain, num_round, watchlist, early_stopping_rounds=50)
