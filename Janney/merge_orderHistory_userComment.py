# -*- coding: utf-8 -*

from tools import local_file_util

userComment_train = [l[0].split(',') for l in [line.split('\"') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/userComment_train.csv')[1:]]]

orderHistory_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderHistory_train.csv')[1:]]

userComment_train_dict = dict([[(line[0], line[1]), [line[2], line[3]]] for line in userComment_train])

merge_res = []
for orderHistory_train_line in orderHistory_train:
    add_line = []
    userId_orderId = (orderHistory_train_line[0], orderHistory_train_line[1])
    add_line = add_line + orderHistory_train_line

    if userId_orderId in userComment_train_dict:
        add_line = add_line + userComment_train_dict[userId_orderId]
    else:
        add_line = add_line + ['', '']
    merge_res.append(add_line)

local_file_util.writeFile('data/merge_orderHistory_userComment.csv', [','.join(line) for line in merge_res])




