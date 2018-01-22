#coding=utf-8
import pandas as pd
import numpy as np
import utils as utils
"""
    code backup
"""

basedir = utils.findPath()

def createFeatureFromUserComment(dataset):
    userComment = pd.read_csv(basedir + "userComment_" + dataset + ".csv")
    orderHistory = pd.read_csv(basedir + "orderHistory_" + dataset + ".csv")
    continent_gdp = pd.read_csv(basedir + "continent_gdp.csv")
    #     userComment.loc[userComment.tags.isnull(), 'tags'] = 0
    #     userComment.loc[userComment.tags.notnull(), 'tags'] = 1
    #     userComment.loc[userComment.commentsKeyWords.isnull(), 'commentsKeyWords'] = 0
    #     userComment.loc[userComment.commentsKeyWords.notnull(), 'commentsKeyWords'] = 1
    orderFuture = pd.read_csv(basedir + "orderFuture_" + dataset + ".csv")
    userOrderHistoryComment = pd.merge(orderHistory, userComment, on=["userid", "orderid"], how='left')
    userOrderHistoryComment = pd.merge(userOrderHistoryComment, continent_gdp, on=["continent", ], how='left')

    userOrderHistoryComment.drop('commentsKeyWords', axis=1, inplace=True)
    userOrderHistoryComment.drop('orderid', axis=1, inplace=True)
    userOrderHistoryComment.drop('city', axis=1, inplace=True)
    userOrderHistoryComment.drop('country', axis=1, inplace=True)
    userOrderHistoryComment.drop('continent', axis=1, inplace=True)

    userOrderHistoryComment_group = userOrderHistoryComment.groupby('userid')

    orderDf = pd.DataFrame(orderFuture['userid'], columns=['userid'])

    #     orderDf = orderDf.join(userOrderHistoryComment_group['orderType'].count(), on='userid')
    #     orderDf.rename(columns={'orderType': 'order_num'}, inplace=True)

    orderDf = orderDf.join(userOrderHistoryComment_group['rating'].mean(), on='userid')
    orderDf.rename(columns={'rating': 'rating_mean'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['rating'].max(), on='userid')
    #     orderDf.rename(columns={'rating': 'rating_max'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['rating'].min(), on='userid')
    #     orderDf.rename(columns={'rating': 'rating_min'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['rating'].std(), on='userid')
    #     orderDf.rename(columns={'rating': 'rating_std'}, inplace=True)

    # Order Time
    #     orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].mean(), on='userid')
    #     orderDf.rename(columns={'orderTime': 'orderTime_mean'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].median(), on='userid')
    #     orderDf.rename(columns={'orderTime': 'orderTime_median'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].min(), on='userid')
    #     orderDf.rename(columns={'orderTime': 'orderTime_min'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['orderTime'].std(), on='userid')
    #     orderDf.rename(columns={'orderTime': 'orderTime_std'}, inplace=True)

    #     orderDf = orderDf.join(userOrderHistoryComment_group['orderType'].sum(), on='userid')
    #     orderDf.rename(columns={'orderType': 'orderType_sum'}, inplace=True)

    orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].mean(), on='userid')
    orderDf.rename(columns={'continent_gdp': 'continent_gdp_mean'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].max(), on='userid')
    #     orderDf.rename(columns={'continent_gdp': 'continent_gdp_max'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].min(), on='userid')
    #     orderDf.rename(columns={'continent_gdp': 'continent_gdp_min'}, inplace=True)
    #     orderDf = orderDf.join(userOrderHistoryComment_group['continent_gdp'].std(), on='userid')
    #     orderDf.rename(columns={'continent_gdp': 'continent_gdp_std'}, inplace=True)

    #     order_month = pd.read_csv(basedir + "order_month_" + dataset + ".csv")
    #     orderDf = pd.merge(orderDf, order_month, on=["userid"], how='left')
    return orderDf


print createFeatureFromUserComment("test").head(3)
