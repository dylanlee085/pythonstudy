#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import re
from lxml import html
from bs4 import BeautifulSoup
import xproxy
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')


def getResponse(url,par=None):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    proxy = xproxy.get_random_ip()
    try:
        response = requests.get(url,params=par,headers=headers,proxies = proxy)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response
    except:
        exit('url 解析失败')

def bs4_info(response):
    soup = BeautifulSoup(response.text,'html.parser')
    content = soup.findAll('tr')
    for tr in content[1:11]:
        game = str(tr.findAll('td')[0].string)
        public_company = str(tr.findAll('td')[1].string)
        type = str(tr.findAll('td')[2].string)
        create_company = str(tr.findAll('td')[3].string)
        ISBN = str(tr.findAll('td')[4].string)
        ISBN_num = str(tr.findAll('td')[5].string)
        values = [game, public_company, type, create_company, ISBN, ISBN_num]
        with open('file.txt', 'a') as f:
            f.write('\n '.join(values))
            f.close

      
        

if __name__ == '__main__':
    keyword=sys.argv[1]
    url = 'http://www.cmmim.com/search/banhao/?key=%s' % keyword 
    response = getResponse(url, par=None)
    print bs4_info(response)
