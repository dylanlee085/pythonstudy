#!/usr/bin/env python
# coding:utf-8 

import requests
from bs4 import BeautifulSoup
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')


def get_province(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text.encode(response.encoding), 'lxml')
    content = content = soup.find_all('tr', class_='provincetr')
    pro_names = []
    pro_urls = []
    for i in content:
        for i in i.find_all('a'):
            pattern = re.compile('<a.*?>(.*?)<br/></a>', re.S)
            name =re.findall(pattern,str(i))[0]
            pro_names.append(name)
            prefix = i.get('href')
            fullurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/' + prefix
            pro_urls.append(fullurl)
    return pro_names, pro_urls


def get_all_City(pro_names,pro_urls):
    for name, url in zip(pro_names, pro_urls):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        response = requests.get(url,headers=headers)
        html = response.text.encode(response.encoding)
#        html = response.text
#        soup = BeautifulSoup(response.text.encode(response.encoding), 'lxml')
#        content = content = soup.find_all('tr', class_='citytr')
        city_names = []
        city_urls = []
        city_codes = []
#        for i in content:
        pattern = re.compile('<tr class=.*?><td><a href=(.*?)>(.*?)</a></td><td><a.*?>(.*?)</a></td></tr>', re.S)
        for i in re.findall(pattern,html):
#            print i
            prefix = i[0]
            code = i[1]
#        city_codes.append(code)
            name = i[2]
            print name
#        city_names.append(name)
        fullurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/' + prefix
#        city_urls.append(fullurl)
#      print city_codes, city_names, city_urls
#        print city_codes, city_names, city_urls
#        print code, name, fullurl



if __name__ == "__main__":
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
    pro_names, pro_urls = get_province(url)
    get_all_City(pro_names,pro_urls)
  
