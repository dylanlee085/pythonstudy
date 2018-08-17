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
    print urls
    return urls

def get_line(urls):
    prefixs = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('div', class_='stie_list')
        for i in content:
            for i in i.find_all('a'):
                prefix = i.get('href')
                prefixs.append(prefix)
    print prefixs
    return prefixs


def get_position(url,prefixs):
    for ii in prefixs:
        fullurl = url + ii
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
            for back in ways[1]:
                print back
            print '总计%d站' % len(positions[1].find_all('a'))
            for b_position in positions[1].find_all('a'):
                print b_position.string
           
if __name__ == '__main__':
    city = 'guangzhou'
    url = 'http://guangzhou.8684.cn'
    urls = get_url(city)
    prefix = get_line(urls)
    print get_position(url, prefix)




