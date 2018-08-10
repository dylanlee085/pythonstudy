#!/usr/bin/env python
# coding: utf-8



import requests
import json
import time
import xproxy


def get_proxy():
    proxy = xproxy.get_random_ip()
    return proxy

def get_html(url):
#def get_html(url,proxy):
#    response = requests.get(url, headers = headers,proxies = proxy)
    response = requests.get(url, headers = headers)
    html = response.text
    return html

#def request_url(html,proxy):
def request_url(html):
    news = json.loads(html)['data']
    urls = []
    for n in news:
        if n["is_feed_ad"] == False:
            print n["title"]
            url = 'https://www.toutiao.com' + n["source_url"]
            urls.append(url)

    for i in urls:
        print i
#        response = requests.get(i, headers = headers,proxies = proxy)
        response = requests.get(i, headers = headers)
        print response.status_code

if __name__ == "__main__": 
    headers = {
        'authority':'www.toutiao.com',
        'method':'GET',
        'path':'/search_content/?offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=3&from=gallery',
        'scheme':'https',
        'accept':'application/json, text/javascript',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'content-type':'application/x-www-form-urlencoded',
        #cookie:UM_distinctid=15f1c13ed94905-013ba6720116af-3e63430c-144000-15f1c13ed95811; uuid="w:cd08eba15729466b8006b1b808652009"; tt_webid=6476830383903573518; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=bvcdrux911518150992381; CNZZDATA1259612802=378713649-1508002287-https%253A%252F%252Fwww.baidu.com%252F%7C1518150741; tt_webid=6476830383903573518
        'referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'x-requested-with':'XMLHttpRequest',
    }
#    url = 'https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A195EB363C3F71C&cp=5B6CAF87B19CAE1&_signature=CalLegAAUspengMhooQJvgmpS2'
    url = "https://www.toutiao.com/api/pc/feed/?category=news_car&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1E52B566D43E0C&cp=5B6D730EB0FCAE1&_signature=wtxt2wAAmbqV6yWAvlpnKcLcbc"
    while True:
#        proxy = xproxy.get_random_ip()
        html = get_html(url)
#        html = get_html(url,proxy)
#        request_url(html,proxy)
        request_url(html)
