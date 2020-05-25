import requests
import json
import datetime
import pandas as pd
from bs4 import BeautifulSoup


def getData():
    url = "https://gw.m.163.com/nc/api/v1/feed/static/h5-normal-list?start=0&size=100"
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 '
                      'Safari/537.36 '
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return json.loads(r.text)['data']


data_news = getData()

lastUpdateTime = str(datetime.date.today())  #
directory = "/data/Space/covid/news/"  # 定义数据保存路径

# 获取中国历史数据及每日新增数据
chinaDayList = pd.DataFrame(data_news["items"])  # 中国历史数据
filename = directory + lastUpdateTime.split(' ')[0] + "_news_data.csv"
header = ["lmodify", "source", "postid", "title", "digest", "url"]
chinaDayList = chinaDayList[header]  # 重排数据框列的顺序
chinaDayList.to_csv(filename, encoding="utf_8_sig", index=False)


def get_news(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 '
                      'Safari/537.36 '
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        s_main = soup.main
        pp = s_main.find_all("p")
        news_str = ''
        for p in pp:
            news_str += p.get_text(strip=True)
        return news_str


news_163 = data_news["items"]
for n1 in news_163:
    news_title = n1["title"]
    news_date = n1["lmodify"]
    news_source = n1["source"]
    news_url = n1["url"]
    news_filename = directory + news_date + "_" + news_source + "_" + news_title + ".txt"
    news_content = get_news(news_url)
    print(news_content)
    with open(news_filename, "w+", encoding="utf_8_sig", newline="") as txt_file:
        txt_file.write(news_content)
