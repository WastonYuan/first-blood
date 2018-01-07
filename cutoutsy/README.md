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