#!/usr/bin/env python
# coding: utf-8


'''
1.无须登录
2.使用requests库
3.直接返回html，不对网页进行处理
'''

import requests
import xproxy
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import json


def get_html(url):
#    proxy = xproxy.get_random_ip()
    try:
        cookie = 'SINAGLOBAL=8890563269122.725.1518338490568; login_sid_t=e892f776dd111de9df7b87930eb5c12f; cross_origin_proto=SSL; _ga=GA1.2.1182793654.1537948032; _gid=GA1.2.1824027628.1537948032; _s_tentry=-; Apache=2548286183114.725.1537948036747; ULV=1537948036757:1:1:1:2548286183114.725.1537948036747:; SCF=Ajlg_C_Mr1kugg0acmL9RVIHmU55-OnemJ6tPUKke9x_BQMeTTw88tj5lZXiBM0qRk-CmLg5wqZA8Z7uR0JiK-0.; SUB=_2A252rzAoDeRhGedI7loU8SnFzjuIHXVV3SbgrDV8PUNbmtBeLXXDkW9NVxoHwVnSPtjiOqWobFcBgQwpso5yfYoy; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWw2KBYM5d52cELDJepwYW45JpX5KzhUgL.Fo2cSKnfeKM4SKM2dJLoI7y2wgpydo5RSBtt; SUHB=0bttpYcnOHSsyk; ALF=1569485810; SSOLoginState=1537949816; wvr=6; WBStorage=e8781eb7dee3fd7f|undefined'
        headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', 'Cookie': cookie}
#        response = requests.get(url, headers=headers, proxies=proxy)
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            html = response.text
            print html
            return html
    except RequestException:
        return None

def para_html(html):
    soup = BeautifulSoup(html,'lxml')
    sc = soup.find_all('script')[12].string
    start = sc.find("(")
    substr = sc[start+1:-1]
    text = json.loads(substr)
    rxml = text["html"]
    soupnew = BeautifulSoup(rxml,'lxml')
    content = soupnew.find_all('div', class_="person_pic")
    for i in content:
        for k in i:
            url = "https:"+ k.get('href')
            nickname = k.get('title')
    print  url, nickname 

def get_user_html(url,name):
    proxy = xproxy.get_random_ip()
    try:
        cookie = 'SINAGLOBAL=8890563269122.725.1518338490568; login_sid_t=e892f776dd111de9df7b87930eb5c12f; cross_origin_proto=SSL; _ga=GA1.2.1182793654.1537948032; _gid=GA1.2.1824027628.1537948032; _s_tentry=-; Apache=2548286183114.725.1537948036747; ULV=1537948036757:1:1:1:2548286183114.725.1537948036747:; SCF=Ajlg_C_Mr1kugg0acmL9RVIHmU55-OnemJ6tPUKke9x_BQMeTTw88tj5lZXiBM0qRk-CmLg5wqZA8Z7uR0JiK-0.; SUB=_2A252rzAoDeRhGedI7loU8SnFzjuIHXVV3SbgrDV8PUNbmtBeLXXDkW9NVxoHwVnSPtjiOqWobFcBgQwpso5yfYoy; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWw2KBYM5d52cELDJepwYW45JpX5KzhUgL.Fo2cSKnfeKM4SKM2dJLoI7y2wgpydo5RSBtt; SUHB=0bttpYcnOHSsyl; ALF=1569485810; SSOLoginState=1537949816; wvr=6; WBStorage=e8781eb7dee3fd7f|undefined'
        headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', 'Cookie': cookie}
#        response = requests.get(url, headers=headers, proxies=proxy)
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            user_html = response.text
            return user_html
    except RequestException:
        return None

def para_user_html(user_html):
    pattern = re.compile('<script>FM.view((.*?))</script>', re.S)
    content =re.findall(pattern,user_html)[23]
    print str(content[0])
    pattern2 = re.compile(r"(\d{4}\年\d{1,2}\月\d{1,2}\日)", re.S)
    date = re.findall(pattern2, content[0])
    print date


if __name__ == '__main__':
    for num in range(1,2):
        url = 'http://s.weibo.com/user/&age=22y&gender=women&region=custom:36:7&&page=%s' % num
        html = get_html(url)
        for value in para_html(html):
            user_html = get_user_html(value[0],value[1])
            para_user_html(user_html)
