#!/usr/bin/env python
#coding:utf-8
'''
目标：1.爬取豆瓣top250 书籍（包含图书名字，作者，出版时间，出版社，售价，图书介绍）
      2：将爬取的数据插入excel
      3：将爬取的数据插入到数据库

步骤: 1.获取网页内容
      2.提取网页内容
      3.保存数据
模块: urllib2
'''

import urllib2
import bs4
import chardet


class BookSpiders:
    def __init__(self):
        self.__headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64)')
    def openurl(self,url):
        opener = urllib2.build_opener()
        opener.addheaders = [self.__headers]
        fileLikeObj = opener.open(url)
        contentString = fileLikeObj.read()
        fileLikeObj.close()
        encodingDictonary = chardet.detect(contentString)
        encoding = encodingDictonary['encoding']
        contentString = contentString.decode(encoding=encoding)
        return contentString
    def get_bookinfo(self,content):
        soup = bs4.BeautifulSoup(content, "html.parser")
        div = soup.findAll('div', class_= "pl2")
        bookname = []
        for i in div:
            name = i.find('a')
            bookname.append(name['title'])
        return bookname


