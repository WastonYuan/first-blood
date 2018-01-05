# -*- coding: utf-8 -*
import pandas as pd
import numpy as np

basedir = "/Users/cutoutsy/workspace/first-blood/"
action_train = pd.read_csv(basedir + "data/trainingset/action_train.csv")

action_train = action_train.sort_values(by='actionTime', ascending=True)
action_train_group = action_train.groupby("userid")
action_train_dict = dict(list(action_train_group))

user_action_dict = dict(list(action_train_group))

timeResultList = []
splitNum = 5
count = 0
for userid, userid_action in user_action_dict.iteritems():
    minTime = userid_action['actionTime'].min()
    maxTime = userid_action['actionTime'].max()
    if minTime == maxTime:
        maxTime = minTime + splitNum
    timeInterval = (maxTime - minTime) / splitNum
    if timeInterval == 0:
        maxTime = minTime + splitNum
        timeInterval = 1
    # plus 1, Divisible 5
    timeSplitList = range(minTime, maxTime + 1, timeInterval)
    # [1474364998 1479034880 1483704762 1488374644 1493044526 1497714408]
    timeSplitList[splitNum] = maxTime + 1
    timeSplitData = []
    for i in range(splitNum):
        timeOneSplit = userid_action[(userid_action['actionTime'] >= timeSplitList[i]) & (userid_action['actionTime'] < timeSplitList[i + 1])]
        timeSplitData = timeSplitData + [timeOneSplit]

    action_count_feat = []
    for item in timeSplitData:
        action_count_feat = action_count_feat + [list(item['actionType']).count(i) for i in range(1, 10)]
    action_count_feat = [userid] + action_count_feat
    print action_count_feat

    timeResultList.append(action_count_feat)



time_columns = ["userid"]
for i in range(splitNum * 9):
    time_columns = time_columns + ["timeAction" + str(i)]
