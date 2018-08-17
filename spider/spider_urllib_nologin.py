#!/usr/bin/env python
# coding: utf-8


'''
1.无须登录
2.使用urllib库
3.直接返回html，不对网页进行处理
'''


import urllib2


#爬取网页内容
def get_html(url):
#需要添加主机头信息，避开返爬虫机制
    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }
#异常判断
    try:
        print '建立请求'
        request = urllib2.Request(url,headers=header)
        print '请求已建立'
        response = urllib2.urlopen(request)

        if response.getcode() == 200:
            print '查看返回的内容'
            return response.read()
        return None
    except Exception as e:
        print e.__str__()
        return None

if __name__ == '__main__':
    url = 'https://www.hao123.com/'
    print get_html(url)
