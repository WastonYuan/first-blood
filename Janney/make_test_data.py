# -*- coding: utf-8 -*
from tools import local_file_util
from itertools import groupby

orderFuture_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/test/orderFuture_test.csv')[1:]]

action_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/test/action_test.csv')[1:]]

orderHistory_comment_train = [line.split(',') for line in local_file_util.readFile('data/merge_orderHistory_userComment_test.csv')]

userProfile_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/test/userProfile_test.csv')[1:]]

def make_origin_train():
    origin_train_line = []
    userProfile_train_dict = dict([(line[0], [line[1], line[2]])for line in userProfile_train])

    orderHistory_comment_train_dict = dict([[user_id, sorted(list([content[1:] for content in hist_content]),key=lambda line:line[1],reverse=True)] for user_id, hist_content in groupby(orderHistory_comment_train, lambda line: line[0])])

    action_train_dict = dict([[user_id, list([content[1] for content in action_content_list])] for user_id, action_content_list in groupby(action_train, lambda line: line[0])])
    for orderFuture_line in orderFuture_train:
        user_id = orderFuture_line[0]
        origin_train_line  =  ['-1', user_id]
        if user_id in userProfile_train_dict:
            origin_train_line = origin_train_line+ (userProfile_train_dict[user_id])
        else:
            origin_train_line = origin_train_line + ['', '']

        hist_num = 3
        left_num = hist_num
        if user_id in orderHistory_comment_train_dict:
            left_num =  hist_num - orderHistory_comment_train_dict[user_id].__len__()
            origin_train_line = origin_train_line + sum(orderHistory_comment_train_dict[user_id][:hist_num], [])
        if left_num >= 1:
            for i in range(left_num):
                origin_train_line = origin_train_line + ['', '', '', '', '', '', '', '']

        if user_id in action_train_dict:
            for i in range(1,10):
                count = action_train_dict[user_id].count(str(i))
                origin_train_line.append(str(count))

        yield origin_train_line





res = list(make_origin_train())

local_file_util.writeFile('data/orgin_test_data.tsv', ['\t'.join(line) for line in res])



origin_train_data = [l.split('\t') for l in local_file_util.readFile('data/orgin_test_data.tsv')]

check = ['\t'.join([str(i) + ':' + l[i] for i in range(l.__len__())]) for l in origin_train_data]

def change_sex(line):
    if line[1] =='女':
        line[1] = '1'
    else:
        line[1] = '0'
    def changeNone2zero(word):
        if word == '':
            return '0'
        else:
            return word
    return [changeNone2zero(ele) for ele in line]

train_data =[change_sex(line) for line in [l[0:1] + l[2:3] + l[5:7] + l[10:11] + l[13:15] + l[18:19] + l[21:23] + l[26:27] + l[28:] for l in origin_train_data]]


local_file_util.writeFile('data/test_data.tsv', ['\t'.join(l) for l in train_data])

