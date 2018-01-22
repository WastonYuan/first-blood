# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import utils as utils
"""
    计算时间间隔、actionType产生的一些特征
"""

basedir = utils.findPath()

def calculateActionTimeInterval(actionfile, savefile):
    action_train = pd.read_csv(basedir + actionfile)
    action_train = action_train.sort_values(by='actionTime', ascending=True)
    action_train_group = action_train.groupby("userid")
    user_action_dict = dict(list(action_train_group))

    count = 0
    actionTimeIntevalTotalResult = []

    for userid, userid_action in user_action_dict.iteritems():
        count = count + 1
        print str(count) + ":" + str(userid)
        actionTimeIntevalResult = []
        actionTimeIntevalResult.append(userid)
        actionTimeList = np.array(userid_action['actionTime'])
        actionTypeList = np.array(userid_action['actionType'])
        timeInterval = np.diff(actionTimeList)
        # print actionTypeList
        # print timeInterval
        # if count == 10:
        #     break
        if len(timeInterval) < 5:
            timeInterval = [0] * (4 - len(timeInterval)) + list(timeInterval)
            timeInterval = np.array(timeInterval)
        firstActionType = userid_action.head(1)['actionType']
        actionTimeIntevalResult = actionTimeIntevalResult + list(firstActionType)
        lastThreeActionType = userid_action.tail(3)['actionType']
        actionTimeIntevalResult = actionTimeIntevalResult + [0] * (3 - len(list(lastThreeActionType))) + list(
            lastThreeActionType)
        actionTimeIntevalResult = actionTimeIntevalResult + [timeInterval.mean(), timeInterval.std(),
                                                             timeInterval.min()] + list(timeInterval[0:1]) + list(
            timeInterval[-4:])
        actionTimeIntevalResult = actionTimeIntevalResult + [timeInterval[-3:].mean(), timeInterval[-3:].std()]

        # 离最近的1-9的时间间隔统计
        IntevalDiff = []
        for i in range(1, 10):
            lastIndex = np.where(actionTypeList == i)
            if len(lastIndex[-1]) == 0:
                action29 = [0, 0, 0, 0]
            else:
                lastIndex = lastIndex[-1][-1]
                if len(timeInterval[lastIndex:]) == 0:
                    action29 = [0, 0, 0, 0]
                else:
                    action29 = [timeInterval[lastIndex:].min(), timeInterval[lastIndex:].mean(),
                                timeInterval[lastIndex:].std(), timeInterval[lastIndex:].max()]
            IntevalDiff = IntevalDiff + action29
        actionTimeIntevalResult = actionTimeIntevalResult + IntevalDiff

        # 距离统计
        actionDis = []
        for i in range(2, 10):
            lastIndex = np.where(actionTypeList == i)
            if len(lastIndex[-1]) == 0:
                actionDistance = 0
            else:
                lastIndex = lastIndex[-1][-1]
                actionDistance = len(timeInterval[lastIndex:])
            actionDis = actionDis + [actionDistance]
        actionTimeIntevalResult = actionTimeIntevalResult + actionDis

        # 距离时间统计
        disTime = []
        for i in range(1, 10):
            lastIndex = np.where(actionTypeList == i)
            if len(lastIndex[-1]) == 0:
                actionTime = 0
            else:
                lastIndex = lastIndex[-1][-1]
                actionTime = timeInterval[lastIndex:].sum()
            disTime = disTime + [actionTime]

        actionTimeIntevalResult = actionTimeIntevalResult + disTime

        # 统计行为1时间间隔的统计值
        type1Result = []
        type1List = np.where(actionTypeList == 1)[-1]
        if len(type1List) < 2:
            type1Result = [0, 0, 0, 0]
        else:
            type1TimeSeq = np.diff(actionTimeList[type1List])
            type1Result = [type1TimeSeq.min(), type1TimeSeq.max(), type1TimeSeq.mean(), type1TimeSeq.std()]
        actionTimeIntevalResult = actionTimeIntevalResult + type1Result


        actionTimeIntevalTotalResult.append(actionTimeIntevalResult)



    columns = ["userid", "firstAction", "last3Action", "last2Action", "last1Action", "intevalMean", "intevalStd",
               "intevalMin", "firstInteval", "lastInteval4", "lastInteval3", "lastInteval2", "lastInteval1",
               "last3IntevalMean", "last3IntevalStd"]
    for i in range(1, 10):
        columns = columns + ["action" + str(i) + "min", "action" + str(i) + "mean", "action" + str(i) + "std",
                             "action" + str(i) + "max"]
    for i in range(2, 10):
        columns = columns + ["action" + str(i) + "Distance"]
    for i in range(1, 10):
        columns = columns + ["action" + str(i) + "DistanceTime"]

    columns = columns + ['type1IntervalMin', 'type1IntervalMax', 'type1IntervalMean', 'type1IntervalStd']

    ActionTimeIntervalDf = pd.DataFrame(np.array(actionTimeIntevalTotalResult), columns=columns)
    ActionTimeIntervalDf.to_csv(basedir + savefile, index=False)

calculateActionTimeInterval("trainingset/action_train.csv", "action_interval_train.csv")
calculateActionTimeInterval("test/action_test.csv", "action_interval_test.csv")