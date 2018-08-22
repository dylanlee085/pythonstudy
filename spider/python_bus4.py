#!/usr/bin/env python
# coding:utf-8

'''
1. 爬取线路
2. 爬取对应线路的站点
3. 爬取站点的经纬度信息
'''


import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_url(city):
    urls = []
    for type1 in range(1,10):
        url = 'http://%s.8684.cn/list%d' % (city, type1)
        urls.append(url)
    for type2 in range(65,91):
        url = 'http://%s.8684.cn/list%s' % (city, chr(type2))
        urls.append(url)
    return urls

def get_line(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('div', class_='stie_list')
        for i in content:
            for i in i.find_all('a'):
                yield i.get('href')

def get_position(url,prefix):
    fullurl = url + prefix
    response = requests.get(fullurl)
    soup = BeautifulSoup(response.text, 'lxml')
    ways = soup.find_all('strong')
    forwards = []
    for forward in ways[0]:
        forwards.append(forward)
    positions = soup.find_all('div', class_='bus_site_layer')
    count1 = '总计%d站' % len(positions[0].find_all('a'))
    global count2
    f_positions = []
    for f_position in positions[0].find_all('a'):
        f_positions.append(f_position.string)
    backs = []
    b_positions = []
    if len(ways) > 1:
        for back in ways[1]:
            backs.append(back)
        count2 = '总计%d站' % len(positions[1].find_all('a'))
        for b_position in positions[1].find_all('a'):
            b_positions.append(b_position.string)
    for i in forwards:
        with open('line.txt', 'a') as f:
            f.write(i + '\n')
    for i in f_positions:
        with open('line.txt', 'a') as f:
            f.write(i + '\n')
    with open('line.txt', 'a') as f:
        f.write(count1 + '\n')
    for i in backs:
        with open('line.txt', 'a') as f:
            f.write(i + '\n')
    for i in b_positions:
        with open('line.txt', 'a') as f:
            f.write(i + '\n')
    with open('line.txt', 'a') as f:
        f.write(count2 + '\n')
    f.close()



           
if __name__ == '__main__':
    city = 'shaoguan'
    url = 'http://%s.8684.cn' % city
    urls = get_url(city)
    for prefix in get_line(urls):
        forwards = get_position(url,prefix)
        
