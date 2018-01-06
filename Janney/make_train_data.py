# -*- coding: utf-8 -*
from tools import local_file_util
from itertools import groupby
import numpy as np

orderFuture_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderFuture_train.csv')[1:]]

action_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/action_train.csv')[1:]]

orderHistory_comment_train = [line.split(',') for line in local_file_util.readFile('data/merge_orderHistory_userComment.csv')]

userProfile_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/userProfile_train.csv')[1:]]

continent_rate_dict = {'大洋洲': 1.4 / 0.33, '欧洲': 19.1 / 7.25, '非洲': 2.2 / 8.69, '北美洲': 21.7 / 4.6, '亚洲': 25.0 / 38.7, '南美洲': 3.6 / 3.5, '南极洲':0.0}

def make_origin_train():
    origin_train_line = []
    userProfile_train_dict = dict([(line[0], line[1:])for line in userProfile_train])

    orderHistory_comment_train_dict = dict([[user_id, sorted(list([content[1:] for content in hist_content]),key=lambda line:line[1],reverse=True)] for user_id, hist_content in groupby(orderHistory_comment_train, lambda line: line[0])])

    action_train_dict = dict([[user_id, list([content[1] for content in action_content_list])] for user_id, action_content_list in groupby(action_train, lambda line: line[0])])
    action_time_dict = dict([[user_id, list([content[2] for content in action_content_list])] for user_id, action_content_list in groupby(action_train, lambda line: line[0])])
    for orderFuture_line in orderFuture_train:
        user_id = orderFuture_line[0]
        origin_train_line  =  [orderFuture_line[1], user_id]
        #userProfile
        if user_id in userProfile_train_dict:
            origin_train_line = origin_train_line+ (userProfile_train_dict[user_id])
        else:
            origin_train_line = origin_train_line + ['', '', '']

        #orderHistory

        hist_num = 3
        left_num = hist_num
        time_feat_list = ['0']*5
        buy_feat_list = ['0']*3
        continent_feat_list = ['0']*4
        if user_id in orderHistory_comment_train_dict:
            left_num =  hist_num - orderHistory_comment_train_dict[user_id].__len__()
            origin_train_line = origin_train_line + sum(orderHistory_comment_train_dict[user_id][:hist_num], []) #get top hist_num order
            time_list = np.array([int(ele[1]) for ele in orderHistory_comment_train_dict[user_id]])
            time_feat_list =[str(num) for num in [time_list.min(), time_list.std(), time_list.mean(), time_list[time_list.size/2], time_list.size]]
            buy_elit_list = np.array([int(ele[2]) for ele in orderHistory_comment_train_dict[user_id]])
            buy_feat_list = [str(num) for num in [buy_elit_list.sum(), buy_elit_list.mean(), buy_elit_list.std()]]
            continent_gdp = np.array([continent_rate_dict[ele[5]] for ele in orderHistory_comment_train_dict[user_id]])
            continent_feat_list = [str(num) for num in [continent_gdp.max(), continent_gdp.min(), continent_gdp.mean(), continent_gdp.std()]]


        if left_num >= 1:
            for i in range(left_num):
                origin_train_line = origin_train_line + ['']*8
        origin_train_line = origin_train_line + time_feat_list + buy_feat_list + continent_feat_list


        #action_train
        action_count_feat = ['0']*9
        action_type_count_feat = ['0']*2
        action_time_feat = ['0']*5
        if user_id in action_train_dict:
            action_count_feat = [str(action_train_dict[user_id].count(str(i))) for i in range(1, 10)]
            action_type_list = [int(int(typ) in range(5,10)) for typ in action_train_dict[user_id]]
            action_type_count_feat = [str(action_type_list.count(t)) for t in range(0, 2)]
            action_time_list = np.array([int(t) for t in action_time_dict[user_id]])
            action_time_feat = [str(num) for num in [action_time_list.mean(), action_time_list.max(), action_time_list.min(), action_time_list.std(), action_time_list.size]]


        origin_train_line = origin_train_line + action_count_feat + action_type_count_feat + action_time_feat



        yield origin_train_line


res = list(make_origin_train())

local_file_util.writeFile('data/orgin_train_data.tsv', ['\t'.join(line) for line in res])


####################################


origin_train_data = [l.split('\t') for l in local_file_util.readFile('data/orgin_train_data.tsv')]

check = ['\t'.join([str(i) + ':' + l[i] for i in range(l.__len__())]) for l in origin_train_data]

city_info = dict([[l[0], l[1]] for l in [line.split('\t') for line in local_file_util.readFile('data/city_info.data')]])

def change_word2num(line):
    sex_index = 1
    city_index = 2
    age_index = 3
    continent_index_list = [6, 10, 14]
    if line[sex_index] =='女':
        line[sex_index] = '1'
    else:
        line[sex_index] = '0'

    if line[city_index] in city_info:
        line[city_index] = city_info[line[city_index]]
    else:
        line[city_index] = '0'

    if line[age_index].__contains__('后'):
        num = int(line[age_index].split('后')[0])
        if(num == 0):
            line[age_index] = str(2018 - 2000 - num)
        else:
            line[age_index] = str(2018 - 1900 - num)

    for continent_index in continent_index_list:
        if line[continent_index] in continent_rate_dict:
            line[continent_index] = str(continent_rate_dict[line[continent_index]])
        else:
            line[continent_index] = '0'


    def changeNone2zero(word):
        if word == '':
            return '0'
        else:
            return word
    return [changeNone2zero(ele) for ele in line]

take_train_data =[l[0:1] +  #label
                    l[2:5] +  #sex city age
                    l[6:8] +  #time order_type
                    l[10:12] +  #continent score
                    l[14:16] +  #time order_type
                    l[18:20] +  #continent score
                    l[22:24] +  #time order_type
                    l[26:28] +  #continent score
                    l[29:]  #min_orderTime to end
                  for l in origin_train_data]

for i in [' '.join(line) for line in [map(lambda t:str(t[1]) + ':' + t[0], zip(line, range(44))) for line in take_train_data]][:300]:print i #test

xgb_train_data =[change_word2num(line) for line in take_train_data]

local_file_util.writeFile('data/train_data.tsv', ['\t'.join(l) for l in xgb_train_data])

