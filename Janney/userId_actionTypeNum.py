# -*- coding: utf-8 -*

from tools import local_file_util

file = map(lambda line:line.split(','), local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/action_train.csv')[1:])


userId_actionTypeList_dict = {}
for line in file:
    if line[0] in userId_actionTypeList_dict:
        temp = userId_actionTypeList_dict[line[0]]
        userId_actionTypeList_dict[line[0]] = temp + [line[2] + ':' +line[1]]
    else:
        userId_actionTypeList_dict[line[0]] = [line[2] + ':' + line[1]]

save_str = sorted(map(lambda key: key + '\t' + str(userId_actionTypeList_dict[key].__len__()) + '\t' + '\t'.join(userId_actionTypeList_dict[key])   , userId_actionTypeList_dict), key=lambda line:int(line.split('\t')[1]), reverse=True)

local_file_util.writeFile('data/userId_actionTypeNum.tsv', save_str)

#userId actionNum(sort) time:actiontye time2:actiontype



