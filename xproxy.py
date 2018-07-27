#!/usr/bin/env python
#encoding:utf-8

import random
import requests
from bs4 import BeautifulSoup

def get_html():
    urls = "http://www.xicidaili.com/"
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    response = requests.get(urls, headers=headers)
    html = response.text
    return html

def get_ip_list():
    html = get_html()
    obj = BeautifulSoup(html,'lxml')
    ip_text = obj.findAll('tr', {'class': 'odd'}) # 获取带有IP地址的表格的所有行
    ip_list = []
    for i in range(len(ip_text)):
        ip_tag = ip_text[i].findAll('td')
        ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text() # 提取出IP地址和端口号
        ip_list.append(ip_port)
    return ip_list

def get_random_ip():
    ip_list = get_ip_list()
    random_ip = 'http://' + random.choice(ip_list)
    proxy_ip = {'http:': random_ip}
    return proxy_ip

if __name__ == '__main__':
    get_random_ip()
