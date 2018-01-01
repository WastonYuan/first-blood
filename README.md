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

0:0	[1:100000002371	2:	3:北京	4:	][5:1000166	6:1493331651	7:0	8:大阪	9:日本	10:亚洲	11:	12:	13:1000164	14:1488884909	15:0	16:大阪	17:日本	18:亚洲	19:5.0	20:主动热情|车辆物资齐全|提前联系|主动搬运行李|耐心等候	21:1000165	22:1488883934	23:0	24:大阪	25:日本	26:亚洲	27:	28:	][29:19	30:0	31:0	32:0	33:14	34:10	35:1	36:4	37:1]

order_history_list|12v: [前3的订单 所有订单时间的最小值/平均值/中位数/标准差/个数 精品订单的个数/概率(均值)/标准差] 洲[1,2,3,5,1]

action_list|6v: 1-4有多少次 5-9有多少次 时间的平均值/最大值/最小值/标准差/总个数





