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

111
