# -*- coding: utf-8 -*
from tools import local_file_util
from itertools import groupby

orderFuture_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderFuture_train.csv')[1:]]

action_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/action_train.csv')[1:]]

orderHistory_comment_train = [line.split(',') for line in local_file_util.readFile('data/merge_orderHistory_userComment.csv')]

userProfile_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/userProfile_train.csv')[1:]]

def make_origin_train():
    origin_train_line = []
    userProfile_train_dict = dict([(line[0], line[1:])for line in userProfile_train])

    orderHistory_comment_train_dict = dict([[user_id, sorted(list([content[1:] for content in hist_content]),key=lambda line:line[1],reverse=True)] for user_id, hist_content in groupby(orderHistory_comment_train, lambda line: line[0])])

    action_train_dict = dict([[user_id, list([content[1] for content in action_content_list])] for user_id, action_content_list in groupby(action_train, lambda line: line[0])])
    for orderFuture_line in orderFuture_train:
        user_id = orderFuture_line[0]
        origin_train_line  =  [orderFuture_line[1], user_id]
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

local_file_util.writeFile('data/orgin_train_data.tsv', ['\t'.join(line) for line in res])



origin_train_data = [l.split('\t') for l in local_file_util.readFile('data/orgin_train_data.tsv')]

check = ['\t'.join([str(i) + ':' + l[i] for i in range(l.__len__())]) for l in origin_train_data]

def change_word2num(line):
    if line[1] =='女':
        line[1] = '1'
    else:
        line[1] = '0'

    if line[2].__contains__('后'):
        num = int(line[2].split('后')[0])
        if(num == 0):
            line[2] = str(2018 - 2000 - num)
        else:
            line[2] = str(2018 - 1900 - num)

    def changeNone2zero(word):
        if word == '':
            return '0'
        else:
            return word
    return [changeNone2zero(ele) for ele in line]

train_data =[change_word2num(line) for line in [l[0:1] + l[2:3] + l[4:5] + l[6:8] + l[11:12] + l[14:16] + l[19:20] + l[22:24] + l[27:28] + l[29:] for l in origin_train_data]]


local_file_util.writeFile('data/train_data.tsv', ['\t'.join(l) for l in train_data])

