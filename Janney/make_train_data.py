
from tools import local_file_util
from itertools import groupby

orderFuture_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderFuture_train.csv')[1:]]

action_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/action_train.csv')[1:]]

orderHistory_comment_train = [line.split(',') for line in local_file_util.readFile('data/merge_orderHistory_userComment.csv')]

userProfile_train = [line.split(',') for line in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/userProfile_train.csv')[1:]]

def make_origin_train():
    origin_train_line = []
    userProfile_train_dict = dict([(line[0], [line[1], line[2]])for line in userProfile_train])

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


