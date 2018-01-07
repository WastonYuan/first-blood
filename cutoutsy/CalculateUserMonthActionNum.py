# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import utils as utils
"""
    Calculate user action count for each month
"""

basedir = utils.findPath()

def calculateUserMonthAction(actionfile, savefile):
    action_train = pd.read_csv(basedir + actionfile)
    action_train['actionTime'] = pd.to_datetime(action_train['actionTime'], unit = 's').dt.month
    action_train_group = action_train.groupby("userid")
    action_train_dict = dict(list(action_train_group))
    count = 0
    monthActionResult = []


    for userid, userid_action in action_train_dict.iteritems():
        monthActionCount = dict(userid_action.groupby('actionTime').size())
        oneMonthActionLine = []
        for i in range(1, 13):
            if i in monthActionCount.keys():
                oneMonthActionLine.append(monthActionCount[i])
            else:
                oneMonthActionLine.append(0)
        monthActionResult.append([userid] + oneMonthActionLine)
        count = count + 1
        print count

    monthColumns = ["userid"]

    for i in range(1, 13):
        monthColumns = monthColumns + ["month" + str(i)]

    monthActionDf = pd.DataFrame(np.array(monthActionResult), columns = monthColumns)
    monthActionDf.to_csv(basedir + "user_month_action.csv", index = False)

calculateUserMonthAction("trainingset/action_train.csv", "user_month__train.csv")
calculateUserMonthAction("test/action_test.csv", "user_month__test.csv")