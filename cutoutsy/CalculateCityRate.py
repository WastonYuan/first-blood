# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import utils as utils
"""
    Calculate city rate
"""

basedir = utils.findPath()

def calculateCityRate(orderHistoryFile, userProfileFile, savefile):
    orderHistory = pd.read_csv(basedir + orderHistoryFile)
    userProfile = pd.read_csv(basedir + userProfileFile)
    userOrderProfile = pd.merge(orderHistory, userProfile, on=["userid"], how='left')

    order_province_group = userOrderProfile.groupby("province").size()
    total = userOrderProfile.shape[0]
    print "total:" + str(total)
    order_province_dict = dict(order_province_group)
    count = 0
    provinceRateResult = []


    for province, num in order_province_dict.iteritems():

        provinceRateResult.append([province, round(num / float(total), 3)])
    print provinceRateResult
    dataColumns = ["province", "province_rate"]


    dataDf = pd.DataFrame(np.array(provinceRateResult), columns = dataColumns)
    dataDf.to_csv(basedir + savefile, index = False)
#
calculateCityRate("trainingset/orderHistory_train.csv", "trainingset/userProfile_train.csv", "city_rate.csv")
# calculateUserMonthAction("test/orderHistory_test.csv", "test/userComment_test.csv", "order_month_test.csv")
