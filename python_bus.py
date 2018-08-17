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
        prefixs = []
        for i in content:
            for i in i.find_all('a'):
                prefix = i.get('href')
#                title = i.get('title')
                prefixs.append(prefix)
        return prefixs


def get_position(url,prefixs):
    for ii in prefixs:
        fullurl = url + ii
        response = requests.get(fullurl)
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find_all('div', class_='bus_site_layer')
        for i in content:
            names = soup.find_all('div', class_='bus_line_txt')
            for names in names:
                for name in names.find_all('strong'):
                    print name.string
                for s in i:
                    position = s.find_all('a')
                    for ss in position:
 #                      print ss.get('href')
                        print ss.string


        return None







if __name__ == '__main__':
    city = 'guangzhou'
    url = 'http://guangzhou.8684.cn'
    urls = get_url(city)
    prefix = get_line(urls)
    print get_position(url, prefix)




