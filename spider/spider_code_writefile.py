#!/usr/bin/env python
# coding:utf-8 

import requests
from bs4 import BeautifulSoup
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
import xproxy
import time


def get_province(url):
#    proxy = xproxy.get_random_ip()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    try:
#        response = requests.get(url,headers=headers,proxies = proxy)
        response = requests.get(url,headers=headers)
        response.encoding = 'gb2312'
        soup = BeautifulSoup(response.text.encode(response.encoding), 'lxml')
        content = content = soup.find_all('tr', class_='provincetr')
        for i in content:
            for i in i.find_all('a'):
                pattern = re.compile('<a.*?>(.*?)<br/></a>', re.S)
                pro_names =re.findall(pattern,str(i))[0]
                prefix = i.get('href')
                pro_urls = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/' + prefix
                yield pro_names, pro_urls
    except:
        exit('url 解析失败') 
            


def get_all_City(pro_names,pro_urls):
#    proxy = xproxy.get_random_ip()
#    for name, url in zip(pro_names, pro_urls):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    try:
#        response = requests.get(pro_urls,headers=headers,proxies = proxy)
        response = requests.get(pro_urls,headers=headers)
        response.encoding = 'gb2312'
        html = response.text
        city_names = []
        city_urls = []
        city_codes = []
        pattern = re.compile('<tr class=.*?><td><a href=\'(.*?)\'>(.*?)</a></td><td><a.*?>(.*?)</a></td></tr>', re.S)
        for i in re.findall(pattern,html):
            code = i[1]
            city_codes.append(code)
            name = i[2]
            city_names.append(name)
            prefix = i[0]
            fullurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/' + prefix
            city_urls.append(fullurl)
        return city_codes, city_names, city_urls
    except:
        exit('url 解析失败')  

def write_into_file(pro_name,city_codes, city_names, city_urls):
    with open('code.txt', 'a') as f:
        f.write(pro_name + '\n')
        for city_code,city_name,city_url in zip(city_codes, city_names, city_urls):
            f.write(city_code +' ') 
            f.write(city_name + ' ') 
            f.write(city_url + '\n') 
        f.close()



if __name__ == "__main__":
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
    for pro_names, pro_urls in  get_province(url):
        pro_name = pro_names
        city_codes, city_names, city_urls = get_all_City(pro_names,pro_urls)
        write_into_file(pro_name,city_codes, city_names, city_urls)
        time.sleep(5)
