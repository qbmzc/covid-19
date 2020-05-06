import requests
import json

def catch_data2():
    # url_2包含全球实时数据及历史数据、中国历史数据及每日新增数据
    url_2 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
    data_2 = json.loads(requests.get(url=url_2).json()['data'])
    return data_2
print(catch_data2())