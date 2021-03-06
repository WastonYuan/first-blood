### 本目录文件运行方式
首先需要将trainingset和test中的所有文件拷贝到data下，这样便于进行训练数据和测试数据的生成。

进入到本目录
```bash
python 文件名.py
```

### 本目录文件说明
#### CalculateActionRate.py
计算用户每个action占总action数的比率，即用户点击1与总点击数比值，用户点击2与总点击数的比值...
计算完成后会在data目录下写入action_rate_train.csv、action_rate_test.csv两个文件，数据格式详情见文件内容

#### CalculateUserMonthActionNum.py
计算用户每个月的action总数
计算完成后会在data目录下写入user_month__train.csv、user_month__test.csv两个文件，数据格式详情见文件内容

特征(100维)：
userid : 用户id  
label : 订单标签  
province_rate: 每个省市占总的省市的比例，缺失值使用中位数填充  
order_num : 用户历史订单数量  
rating_mean : 历史订单评分均值  
orderType_sum : 历史订单为1(精品)的数量
continent_gdp_mean : 历史订单去的洲的GDP均值  
month1 : 用户在1月份的行为数量  
month2 : 用户在2月份的行为数量  
month3 : 用户在3月份的行为数量  
month4 : 用户在4月份的行为数量  
month5 : 用户在5月份的行为数量  
month6 : 用户在6月份的行为数量  
month7 : 用户在7月份的行为数量  
month8 : 用户在8月份的行为数量  
month9 : 用户在9月份的行为数量  
month10 : 用户在10月份的行为数量  
month11 : 用户在11月份的行为数量  
month12 : 用户在12月份的行为数量  
actionType1rate : 用户行为1占总行为的比率  
actionType24Rate : 用户行为2~4占总行为的比率  
actionType5rate : 用户行为5占总行为的比率  
actionType6rate : 用户行为6占总行为的比率  
actionType7rate : 用户行为7占总行为的比率  
actionType8rate : 用户行为8占总行为的比率  
actionType9rate : 用户行为9占总行为的比率  
firstAction : 用户行为序列中第一个行为

last3Action : 用户行为序列中倒数第3个行为

last2Action : 用户行为序列中倒数第二个行为

last1Action : 用户行为序列中最后一个行为

intevalMean : 用户行为时间间隔的均值

intevalStd : 用户行为时间间隔的方差

intevalMin : 用户行为时间间隔的最小值

firstInteval : 用户行为时间间隔序列中第一个时间间隔

lastInteval4 : 用户行为时间间隔序列中倒数第4个时间间隔

lastInteval3 : 用户行为时间间隔序列中倒数第3个时间间隔

lastInteval2 : 用户行为时间间隔序列中倒数第2个时间间隔

lastInteval1 : 用户行为时间间隔序列中倒数第1个时间间隔

last3IntevalMean : 用户行为时间间隔序列中最后三个时间间隔的均值

last3IntevalStd : 用户行为时间间隔序列中最后三个时间间隔的方差

action2min : 用户行为时间间隔序列中离最近行为2后的时间间隔的最小值

action2mean : 用户行为时间间隔序列中离最近行为2后的时间间隔的均值

action2std : 用户行为时间间隔序列中离最近行为2后的时间间隔的方差

action2max : 用户行为时间间隔序列中离最近行为2后的时间间隔的最大值

action3min : 用户行为时间间隔序列中离最近行为3后的时间间隔的最小值

action3mean : 用户行为时间间隔序列中离最近行为3后的时间间隔的均值

action3std : 用户行为时间间隔序列中离最近行为3后的时间间隔的方差

action3max : 用户行为时间间隔序列中离最近行为3后的时间间隔的最大值

action4min : 用户行为时间间隔序列中离最近行为4后的时间间隔的最小值

action4mean : 用户行为时间间隔序列中离最近行为4后的时间间隔的均值

action4std : 用户行为时间间隔序列中离最近行为4后的时间间隔的方差

action4max : 用户行为时间间隔序列中离最近行为4后的时间间隔的最大值

action5min : 用户行为时间间隔序列中离最近行为5后的时间间隔的最小值

action5mean : 用户行为时间间隔序列中离最近行为5后的时间间隔的均值

action5std : 用户行为时间间隔序列中离最近行为5后的时间间隔的方差

action5max : 用户行为时间间隔序列中离最近行为5后的时间间隔的最大值

action6min : 用户行为时间间隔序列中离最近行为6后的时间间隔的最小值

action6mean : 用户行为时间间隔序列中离最近行为6后的时间间隔的均值

action6std : 用户行为时间间隔序列中离最近行为6后的时间间隔的方差

action6max : 用户行为时间间隔序列中离最近行为6后的时间间隔的最大值

action7min : 用户行为时间间隔序列中离最近行为7后的时间间隔的最小值

action7mean : 用户行为时间间隔序列中离最近行为7后的时间间隔的均值

action7std : 用户行为时间间隔序列中离最近行为7后的时间间隔的方差

action7max : 用户行为时间间隔序列中离最近行为7后的时间间隔的最大值

action8min : 用户行为时间间隔序列中离最近行为8后的时间间隔的最小值

action8mean : 用户行为时间间隔序列中离最近行为8后的时间间隔的均值

action8std : 用户行为时间间隔序列中离最近行为8后的时间间隔的方差

action8max : 用户行为时间间隔序列中离最近行为8后的时间间隔的最大值

action9min : 用户行为时间间隔序列中离最近行为9后的时间间隔的最小值

action9mean : 用户行为时间间隔序列中离最近行为9后的时间间隔的均值

action9std : 用户行为时间间隔序列中离最近行为9后的时间间隔的方差

action9max : 用户行为时间间隔序列中离最近行为9后的时间间隔的最大值

action2Distance : 用户行为序列中距离最近2的距离

action3Distance : 用户行为序列中距离最近3的距离

action4Distance : 用户行为序列中距离最近4的距离

action5Distance : 用户行为序列中距离最近5的距离

action6Distance : 用户行为序列中距离最近6的距离

action7Distance : 用户行为序列中距离最近7的距离

action8Distance : 用户行为序列中距离最近8的距离

action9Distance : 用户行为序列中距离最近9的距离

action1DistanceTime : 用户行为时间序列中距离1的时间间隔

action2DistanceTime : 用户行为时间序列中距离2的时间间隔

action3DistanceTime : 用户行为时间序列中距离3的时间间隔

action4DistanceTime : 用户行为时间序列中距离4的时间间隔

action5DistanceTime : 用户行为时间序列中距离5的时间间隔

action6DistanceTime : 用户行为时间序列中距离6的时间间隔

action7DistanceTime : 用户行为时间序列中距离7的时间间隔

action8DistanceTime : 用户行为时间序列中距离8的时间间隔

action9DistanceTime : 用户行为时间序列中距离9的时间间隔

tagScore: 用户历史订单tag转换为数值，一个好的标签+1，一个差的标签-2

type1IntervalMin: 用户行为1时间间隔的最小值

type1IntervalMax: 用户行为1时间间隔的最大值

type1IntervalMean: 用户行为1时间间隔的均值

type1IntervalStd: 用户行为1时间间隔的标准差