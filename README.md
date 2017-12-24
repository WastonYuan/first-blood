# first-blood

action_train.csv
用户id，行为类型(1-9)，发生时间
userid,actionType,actionTime
100000000013,1,1474300753

userProfile_train.csv
用户id、性别、省份、年龄段
userid,gender,province,age
100000001023,男,北京,60后

orderHistory_train.csv
用户id，订单id，订单时间，订单类型，旅游城市，国家，大陆
userid,orderid,orderTime,orderType,city,country,continent
100000000013,1000015,1481714516,0,柏林,德国,欧洲

userComment_train.csv
用户id，订单id，评分，标签，评论内容
userid,orderid,rating,tags,commentsKeyWords
100000003639,1000202,5.0,主动热情|提前联系,"['非常','满意']"

orderFuture_train.csv
用户id, 订单类型
100000000013,0

label 特征list
1 用户id 性别 省份 年龄 订单数据list(order_history:订单时间，订单类型，旅游城市，国家，大陆, 评分，标签，tags, comments)... 行为数据list(action: 行为类型， 发生时间)


first character decssion - 18v
0/1 用户id(must) 性别(男:0/女:1) 年龄(2018-19xx) 订单时间(时间戳) 订单类型(0/1) 订单时间(时间戳) 订单类型(0/1) 订单时间(时间戳) 订单类型(0/1) 行为1(数量) 行为2(数量) 行为3(数量) 行为4 行为5 行为6 行为7 行为8 行为9

sample train_v1.data:
1 1:1355501 2:0 3:28 4:1496666621 5:0 6:1486666621 7:1 8:14655555521 9:1 10:99 11:66 12:22 13:33 14:66 15:66 16:33 17:22 18:1
0 1:1355502 2:1 3:18 18:5


