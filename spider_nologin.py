#!/usr/bin/env python
#coding:utf-8


import urllib2



#方法一
response = urllib2.urlopen('http://www.baidu.com') #访问网址,参数必须为网址
print response.read() #读取网页内容

#方法二
request = urllib2.Request("http://www.baidu.com") #构造一个request请求
response = urllib2.urlopen(request)
print response.read()  

