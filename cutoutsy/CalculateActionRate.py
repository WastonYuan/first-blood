# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import utils as utils
"""
    Calculate user action rate(用户点击1与总点击数比值...)
"""

basedir = utils.findPath()
def calculateActionRate(actionfile, savefile):
    # action_train = pd.read_csv(basedir + "trainingset/action_train.csv")
    action_train = pd.read_csv(basedir + actionfile)
    action_train_group = action_train.groupby("userid")
    action_train_dict = dict(list(action_train_group))
    count = 0
    actionRateResult = []
    for userid, userid_action in action_train_dict.iteritems():
        actionTotal = len(userid_action)
        userActionType = dict(userid_action.groupby('actionType').size())
        oneActionRateResult = []

        if userActionType.has_key(1):
            oneActionRateResult.append(userActionType[1])
            oneActionRateResult.append(round(userActionType[1] / float(actionTotal), 3))
        else:
            oneActionRateResult.append(0)
            oneActionRateResult.append(0.0)

        actionType24Count = 0
        for i in range(2, 5):
            if userActionType.has_key(i):
                actionType24Count = actionType24Count + userActionType[i]
            else:
                actionType24Count = actionType24Count + 0
        oneActionRateResult.append(actionType24Count)
        oneActionRateResult.append(round(actionType24Count / float(actionTotal), 3))

        for i in range(5, 10):
            if userActionType.has_key(i):
                oneActionRateResult.append(userActionType[i])
                oneActionRateResult.append(round(userActionType[i] / float(actionTotal), 3))
            else:
                oneActionRateResult.append(0)
                oneActionRateResult.append(0.0)
        actionRateResult.append([userid] + oneActionRateResult)
        #print [userid] + oneActionRateResult
        count = count + 1
        print count

    actionRateColumns = ["userid", "actionType1Count", "actionType1Rate", "actionType24Count", "actionType24Rate"]
    for i in range(5, 10):
        actionRateColumns = actionRateColumns + ["actionType" + str(i) + "Count"] + ["actionType" + str(i) + "Rate"]

    actionRateDf = pd.DataFrame(np.array(actionRateResult), columns = actionRateColumns)
    # 2~4是浏览产品，无先后关系，统计在一起
    # actionRateDf['actionType24'] = actionRateDf['actionType2Count'] + actionRateDf['actionType3Count'] + actionRateDf['actionType4Count']
    # actionRateDf.drop('actionType2Count', axis=1, inplace=True)
    # actionRateDf.drop('actionType3Count', axis=1, inplace=True)
    # actionRateDf.drop('actionType4Count', axis=1, inplace=True)

    actionRateDf.to_csv(basedir + savefile, index = False)

calculateActionRate("trainingset/action_train.csv", "action_rate_train.csv")
calculateActionRate("test/action_test.csv", "action_rate_test.csv")
