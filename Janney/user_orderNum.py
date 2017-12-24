# -*- coding: utf-8 -*
#统计每个用户的订单数量
from tools import local_file_util

file =map(lambda line: line.split(','), local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderHistory_train.csv')[1:])


userId_orderId_list = map(lambda line:(line[0], line[1]), file)


dic = {}

#userid: list(orderid1, oderid2)

for userId_orderId in userId_orderId_list:
    if userId_orderId[0] in dic:
        temp = dic[userId_orderId[0]]+ [userId_orderId[1]]
        dic[userId_orderId[0]] = temp
    else:
        dic[userId_orderId[0]] = [userId_orderId[1]]


userId_oderNum = sorted(map(lambda key: (key, dic[key].__len__()), dic), key=lambda tuple: tuple[1], reverse=True)

res_save_str = map(lambda line: line[0] + '\t' + str(line[1]), userId_oderNum)

local_file_util.writeFile('data/user_orderNum.tsv', res_save_str)