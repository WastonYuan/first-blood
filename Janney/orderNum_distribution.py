# -*- coding: utf-8 -*

from tools import local_file_util

file = map(lambda line: line.split('\t'), local_file_util.readFile('data/user_orderNum.tsv'))

orderNum_userId_dic = {}

for userId_orderNum in file:
    if userId_orderNum[1] in orderNum_userId_dic:
        temp = orderNum_userId_dic[userId_orderNum[1]] + [userId_orderNum[0]]
        orderNum_userId_dic[userId_orderNum[1]] = temp
    else:
        orderNum_userId_dic[userId_orderNum[1]] = [userId_orderNum[0]]


orderNum_userIdNum = sorted(map(lambda key: (key, orderNum_userId_dic[key].__len__()), orderNum_userId_dic), key=lambda tuple: tuple[1], reverse=True)

save_str = map(lambda line: line[0] + '\t' + str(line[1]), orderNum_userIdNum)

local_file_util.writeFile('data/orderNum_userIdNum.tsv', save_str)

