import xgboost as xgb

bst = xgb.Booster({'nthread': 4})
bst.load_model('data/xgb_model/xgb_v1.model')

import numpy as np

data = np.loadtxt('data/test_data.tsv', delimiter='\t')

test_x = data[:,1:]
test_y = data[:,0]
dtest = xgb.DMatrix(test_x, label=test_y)

eval = bst.predict(dtest)



