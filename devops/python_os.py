#!/usr/bin/env python
# coding:utf-8


import urllib2

def clear():
    print (u'内容较多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if OS == u'Windows':
        os.system('cls')
    else:
        os.system('clear')

def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib2.urlopen(url, timeout=3)
    except urllib2.URLError:
        print (u'网络地址错误')
        exit()

    with open('./baidu.txt', 'w') as fp:
        fp.write(response.read())

    print response.geturl()
    print response.getcode()
    print response.info()

if __name__ == '__main__':
    linkBaidu()

