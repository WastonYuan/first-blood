# -*- coding: utf-8 -*

from tools import local_file_util
import numpy as np
from itertools import groupby

orderFuture = [l.split(',') for l in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderFuture_train.csv')[1:]]

userid_label_dict = dict(orderFuture)
target_userid = [l[0] for l in orderFuture]

country_gdp_dict = dict([l.split('\t') for l in local_file_util.readFile('data/Jack/country_gdp.tsv')])

orderFuture_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderFuture_train.csv')[1:]]

orderHistory_comment_train = [line.split(',') for line in local_file_util.readFile('data/merge_orderHistory_userComment.csv')]
orderHistory_comment_train_dict = dict([[user_id, sorted(list([content[1:] for content in hist_content]),key=lambda line:line[1],reverse=True)] for user_id, hist_content in groupby(orderHistory_comment_train, lambda line: line[0])])

last_country_num = 3

def get_userid_country_feat_list(userid):

    top_country_gdp_series_feat = [0.0]*3
    country_gdp_statistics_feat = [0.0]*5

    if userid in orderHistory_comment_train_dict:
        country_gdp_list = [int(country_gdp_dict[l[4]]) for l in orderHistory_comment_train_dict[userid]]
        country_gdp_arr = np.array(country_gdp_list)
        top_country_gdp_series_feat = country_gdp_list[:last_country_num] +  [0]*(last_country_num - country_gdp_list[:last_country_num].__len__()) #3v top3 城市人均gdp值
        country_gdp_statistics_feat = [country_gdp_arr.max(), country_gdp_arr.min(), country_gdp_arr.mean() ,country_gdp_arr.std(), set(country_gdp_list).__len__()] #5v 城市人均gdp最大,最小,均值,标准差,城市个数(去重)

    return [str(i) for i in top_country_gdp_series_feat + country_gdp_statistics_feat]


local_file_util.writeFile('data/country_feat.tsv', [userid_label_dict[userid] + '\t' + '\t'.join(get_userid_country_feat_list(userid)) for userid in target_userid])