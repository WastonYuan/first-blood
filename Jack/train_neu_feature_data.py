
from tools import local_file_util
import numpy as np
import datetime
from itertools import groupby


action_train = [l.split(',') for l in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/action_train.csv')[1:]]

action_train_dict = dict([[user_id, list([(content[1], content[2]) for content in action_content_list])] for user_id, action_content_list in groupby(action_train, lambda line: line[0])])


time_stamp_arr = np.array([int(l[2]) for l in action_train])

print(datetime.datetime.fromtimestamp(time_stamp_arr.min()).strftime('%Y-%m-%d %H:%M:%S'))

time_stamp_arr.max() - time_stamp_arr.min()

time_split_arr = np.linspace(start=time_stamp_arr.min(), stop=time_stamp_arr.max(), num=201)

time_range_list = [(v, w) for v, w in zip(time_split_arr[:-1], time_split_arr[1:])]

for i in [str(time_range_list.index(t)) + '\t' + datetime.datetime.fromtimestamp(t[0]).strftime('%Y-%m-%d %H:%M:%S') + '\t' +  datetime.datetime.fromtimestamp(t[1]).strftime('%Y-%m-%d %H:%M:%S') for t in time_range_list]: print i

orderFuture = [l.split(',') for l in local_file_util.readFile('bigdata/huangbaoche/huangbaoche_unzip/trainingset/orderFuture_train.csv')[1:]]

target_userid = [l[0] for l in orderFuture]

def get_count_feat(userid):
    print user_id
    feature_list = [[int(0)]*9 for i in range(200)]
    if userid in action_train_dict:
        action_list = action_train_dict[userid]
        for action in action_list:
            action_time = int(action[1])
            action_type_index = int(action[0]) - 1
            def get_time_range_index(time):
                for index in range(time_range_list.__len__()):
                    start = time_range_list[index][0]
                    end = time_range_list[index][1]
                    if time >= start and time <= end:
                        return index
                    else:
                        assert 'no time'
            time_range_index = get_time_range_index(action_time)
            feature_list[time_range_index][action_type_index] += 1
    return feature_list


def get_feat(userid):
    count_feat = get_count_feat(userid)
    rate_feat = [[float(t)/(sum(l)+1e-10) for t in l] for l in count_feat]
    return sum([sum(l, []) for l in zip(count_feat, rate_feat)], [])

local_file_util.writeFile('data/neuro_feat.tsv', [user_id + '\t' + '\t'.join([str(feat) for feat in get_feat(user_id)]) for user_id in target_userid])




