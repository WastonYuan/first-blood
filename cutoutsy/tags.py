#coding=utf-8
import pandas as pd
import numpy as np
import utils as utils
"""
    Calculate city rate
"""

basedir = utils.findPath()

# 获得所有的Tags
def getAllTags():
    userComment_train = pd.read_csv(basedir + "userComment_train.csv")['tags'].dropna(axis=0, how='all')
    userComment_test = pd.read_csv(basedir + "userComment_test.csv")['tags'].dropna(axis=0, how='all')
    tags_set_train = set()
    tags_set_test = set()
    for index in userComment_train:
        tags = index.split('|')
        for i in tags:
            if i not in tags_set_train:
                print i
                tags_set_train.add(i)
    print '-------'
    for ele in userComment_test:
        tags = ele.split('|')
        for i in tags:
            if i not in tags_set_train:
                print i
                tags_set_test.add(i)

    c = tags_set_test | tags_set_train
    print c.__len__()

# 将标签转化为数值
def tagConvertNum(userCommentFile, saveFile):
    tagGood = pd.read_csv(basedir + "tags_good.csv")['tags']
    tagMid = pd.read_csv(basedir + "tags_Mid.csv")['tags']
    tagBad = pd.read_csv(basedir + "tags_bad.csv")['tags']
    userComment = pd.read_csv(basedir + userCommentFile).loc[:, ['userid', 'tags']]
    userComment = userComment.dropna(axis=0, how='any')
    userCommentDict = dict(list(userComment.groupby('userid')))
    count = 0
    tagScoreResult = []
    for userid, tagContent in userCommentDict.iteritems():
        tagScore = 0;
        count = count + 1
        print count
        # if count == 10:
        #     break
        allTags = tagContent['tags']
        for tags in allTags:
            for oneTag in tags.split('|'):
                # print oneTag
                if oneTag in tagGood.values:
                    tagScore = tagScore + 1
                elif oneTag in tagBad.values:
                    tagScore = tagScore - 2
        tagScoreResult.append([userid, tagScore])
        # print str(userid) + ": " + str(tagScore)
    columns = ['userid', 'tagScore']
    df = pd.DataFrame(np.array(tagScoreResult), columns=columns)
    df.to_csv(basedir + saveFile, index=False)

tagConvertNum("userComment_train.csv", "user_tagScore_train.csv")
tagConvertNum("userComment_test.csv", "user_tagScore_test.csv")