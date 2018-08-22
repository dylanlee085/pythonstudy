#!/usr/bin/env python
# coding: utf-8


'''
1.无须登录
2.使用requests库
3.直接返回html，不对网页进行处理
'''

import requests

def get_html(url):
    try:
        headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            return response.text
    except RequestException:
        return None

if __name__ == '__main__':
    url = 'https://www.hao123.com/'
    print get_html(url) 
