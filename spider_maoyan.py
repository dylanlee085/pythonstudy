#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import re
from lxml import html
from bs4 import BeautifulSoup
import xproxy

url = 'http://maoyan.com/board/4?' 

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
    names = [i.a.string for i in soup.find_all(name='p',attrs='name')]
    stars = [i.string.strip() for i in soup.find_all(name='p',attrs='star')]
    times = [i.string for i in soup.find_all(name='p',attrs='releasetime')] 
    scores_tag = [i.contents for i in soup.find_all(name='p',attrs='score')]
    scores = [item[0].string + item[1].string for item in scores_tag]
    return names,stars,times,scores
        

names,stars,times,scores = [],[],[],[]

for i in range(10):
    response = getResponse(url,par={'offset':str(10*i)})
    name,star,time,score = bs4_info(response)
    names += name
    stars += star
    times += time
    scores += score

for i in range(len(names)):
    print names[i], stars[i], times[i], scores[i]
