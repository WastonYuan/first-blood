# -*- coding: utf-8 -*

import numpy as np
import xgboost as xgb

data = np.loadtxt('data/train_data.tsv', delimiter='\t')

train_x = data[:int(data.shape[0]*0.7),1:]
train_y = data[:int(data.shape[0]*0.7),0]
test_x = data[int(data.shape[0]*0.7):,1:]
test_y = data[int(data.shape[0]*0.7):,0]
dtrain = xgb.DMatrix(train_x, label=train_y)
dtest = xgb.DMatrix(test_x, label=test_y)

params = {'gamma':2.0,'nthread':8, 'max_depth':15, 'eta':0.03, 'silent':1, 'objective':'binary:logistic'}

watchlist = [(dtrain,'train'), (dtest,'eval')]



num_round = 50
bst = xgb.train(params, dtrain, num_round, watchlist, early_stopping_rounds=50)

bst.predict(dtrain)

save_train_x = data[:,1:]
save_train_y = data[:,0]
save_dtrain = xgb.DMatrix(save_train_x, label=save_train_y)
save_bst = xgb.train(params, save_dtrain, num_round, watchlist, early_stopping_rounds=50)

save_bst.save_model('xgb_model/xgb_v1.model')