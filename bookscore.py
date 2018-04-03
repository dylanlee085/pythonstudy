#!/usr/bin/env python
#coding:utf-8

from BookSpider import BookSpiders


bookspider = BookSpiders()
for i in range(0,250,25):
    url="https://book.douban.com/top250?start=%d" % i
    contentHTML = bookspider.openurl(url)
    for name in  bookspider.get_bookinfo(contentHTML):
        print name

