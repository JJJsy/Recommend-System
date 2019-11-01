import pandas as pd
import time

# 数据加载
data = pd.read_csv('./BreadBasket_DMS.csv')
# 统一小写
data['Item'] = data['Item'].str.lower()
print(data.head(5))
# 去掉none项
data = data.drop(data[data.Item == 'none'].index)
print(data.head(5))
