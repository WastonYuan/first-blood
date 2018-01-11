# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import utils as utils
"""
    Calculate user order count for each month
"""

basedir = utils.findPath()

def calculateUserMonthAction(orderHistoryFile, userCommentFile, savefile):
    orderHistory = pd.read_csv(basedir + orderHistoryFile)
    userComment = pd.read_csv(basedir + userCommentFile)
    userOrderHistoryComment = pd.merge(orderHistory, userComment, on=["userid", "orderid"], how='left')
    userOrderHistoryComment['orderTime'] = pd.to_datetime(userOrderHistoryComment['orderTime'], unit = 's').dt.month
    action_train_group = userOrderHistoryComment.groupby("userid")
    action_train_dict = dict(list(action_train_group))
    count = 0
    monthActionResult = []


    for userid, userid_action in action_train_dict.iteritems():
        monthActionCount = dict(userid_action.groupby('orderTime').size())
        oneMonthActionLine = []
        for i in range(1, 13):
            if i in monthActionCount.keys():
                oneMonthActionLine.append(monthActionCount[i])
            else:
                oneMonthActionLine.append(0)
        monthActionResult.append([userid] + oneMonthActionLine)
        print oneMonthActionLine
        count = count + 1
        print count

    monthColumns = ["userid"]

    for i in range(1, 13):
        monthColumns = monthColumns + ["order_month" + str(i)]

    monthActionDf = pd.DataFrame(np.array(monthActionResult), columns = monthColumns)
    monthActionDf.to_csv(basedir + savefile, index = False)

calculateUserMonthAction("trainingset/orderHistory_train.csv", "trainingset/userComment_train.csv", "order_month_train.csv")
calculateUserMonthAction("test/orderHistory_test.csv", "test/userComment_test.csv", "order_month_test.csv")
