#! /usr/bin/env python
# coding: utf-8

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://www.toutiao.com/stream/widget/local_weather/city/'
response = requests.get(url).text
data = json.loads(response)
news = data['data']
for i in news.items():
    with open('toutiao_code.txt', 'a') as f:
        f.write(i[0] + '\n')
    for i in i[1].items():
        with open('toutiao_code.txt', 'a') as f:
            content = str(i[0]) + str(i[1])
            f.write(content + '\n')
