### 本目录文件运行方式
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

特征：

userid                 object

label                   int64

age                     int64

city_gdp              float64

order_num             float64

rating_mean           float64

rating_max            float64

rating_min            float64

rating_std            float64

orderType_sum         float64

continent_gdp_mean    float64

continent_gdp_max     float64

continent_gdp_min     float64

continent_gdp_std     float64

month1                  int64

month2                  int64

month3                  int64

month4                  int64

month5                  int64

month6                  int64

month7                  int64

month8                  int64

month9                  int64

month10                 int64

month11                 int64

month12                 int64

actionType1Count      float64

actionType1rate       float64

actionType2Count      float64

actionType2rate       float64

actionType3Count      float64

actionType3rate       float64

actionType4Count      float64

actionType4rate       float64

actionType5Count      float64

actionType5rate       float64

actionType6Count      float64

actionType6rate       float64

actionType7Count      float64

actionType7rate       float64

actionType8Count      float64

actionType8rate       float64

actionType9Count      float64

actionType9rate       float64