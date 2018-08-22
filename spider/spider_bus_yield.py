#!/usr/bin/env python
# coding:utf-8

'''
1. 爬取线路
2. 爬取对应线路的站点
3. 爬取站点的经纬度信息
'''


import requests
from bs4 import BeautifulSoup


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
    for forward in ways[0]:
        print  forward
    positions = soup.find_all('div', class_='bus_site_layer')
    print '总计%d站' % len(positions[0].find_all('a'))
    for f_position in positions[0].find_all('a'):
        print f_position.string
    if len(ways) > 1:
        print '总计%d站' % len(positions[1].find_all('a'))
        for back in ways[1]:
            print back
        for b_position in positions[1].find_all('a'):
            print b_position.string

           
if __name__ == '__main__':
    city = 'yichun'
    url = 'http://%s.8684.cn' % city
    urls = get_url(city)
    for prefix in get_line(urls):
        get_position(url,prefix)
        




