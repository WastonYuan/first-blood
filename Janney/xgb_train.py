# -*- coding: utf-8 -*

from tools import local_file_util

origin_train_data = [l.split('\t') for l in local_file_util.readFile('data/orgin_train_data.tsv')]

check = ['\t'.join([str(i) + ':' + l[i] for i in range(l.__len__())]) for l in origin_train_data]

def change_sex(line):
    if line[1] =='女':
        line[1] = '1'
    else:
        line[1] = '0'
    def changeNone2zero(word):
        if word == '':
            return '0'
        else:
            return word
    return [changeNone2zero(ele) for ele in line]

train_data =[change_sex(line) for line in [l[0:1] + l[2:3] + l[5:7] + l[10:11] + l[13:15] + l[18:19] + l[21:23] + l[26:27] + l[28:] for l in origin_train_data]]


local_file_util.writeFile('data/train_data.tsv', ['\t'.join(l) for l in train_data])

import numpy as np
import xgboost as xgb

data = np.loadtxt('data/train_data.tsv', delimiter='\t')

train_x = data[:int(data.shape[0]*0.7),1:]
train_y = data[:int(data.shape[0]*0.7),0]
test_x = data[int(data.shape[0]*0.7):,1:]
test_y = data[int(data.shape[0]*0.7):,0]
dtrain = xgb.DMatrix(train_x, label=train_y)
dtest = xgb.DMatrix(test_x, label=test_y)

param = {'gamma':2.0,'nthread':8, 'max_depth':15, 'eta':0.03, 'silent':1, 'objective':'multi:softprob' ,'num_class':105}