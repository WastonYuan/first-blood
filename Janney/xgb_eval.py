import xgboost as xgb

bst = xgb.Booster({'nthread': 4})
bst.load_model('xgb_model/xgb_v1.model')

import numpy as np

data = np.loadtxt('data/test_data.tsv', delimiter='\t')

test_x = data[:,1:]
test_y = data[:,0]
dtest = xgb.DMatrix(test_x, label=test_y)

eval = bst.predict(dtest)

from tools import local_file_util
file = [line.split(',')[0] for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/test/orderFuture_test.csv')[1:]]

res = [line[0] + ',' + str(line[1]) for line in zip(file, list(eval))]
res.insert(0, 'userid,orderType')

local_file_util.writeFile('data/submit.csv', res)

