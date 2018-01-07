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
        for i in range(1, 10):
            if userActionType.has_key(i):
                oneActionRateResult.append(round(userActionType[i] / float(actionTotal), 3))
            else:
                oneActionRateResult.append(0.0)
        actionRateResult.append([userid] + oneActionRateResult)
        #print [userid] + oneActionRateResult
        count = count + 1
        print count

    actionRateColumns = ["userid"]
    for i in range(1, 10):
        actionRateColumns = actionRateColumns + ["actionType" + str(i)]

    actionRateDf = pd.DataFrame(np.array(actionRateResult), columns = actionRateColumns)
    actionRateDf.to_csv(basedir + savefile, index = False)

calculateActionRate("trainingset/action_train.csv", "action_rate_train.csv")
calculateActionRate("test/action_test.csv", "action_rate_test.csv")
