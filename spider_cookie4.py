#!/usr/bin/env python
#coding:utf-8


import urllib2
import urllib
import cookielib


filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({})
response = opener.open('http://www.baidu.com',postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'http://news.baidu.com'
result = opener.open(gradeUrl)
print result.read()
