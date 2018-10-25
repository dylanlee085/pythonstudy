#! /usr/bin/env python
# coding: utf-8


import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from lxml import etree

class spider(object):

    # 获取url对应的网页源码
    def getsource(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        sourceHtml = requests.get(url, headers=headers)
        return sourceHtml.text

    # 改变链接的地址页
    def chagnePage(self,orginalStr):
        currentPage = int(re.search('page=(\d+)', orginalStr, re.S).group(1))
        pageGroup = []
        for i in range(currentPage, currentPage + 3):
            link = re.sub('page=\d+', 'page=%s' % i, orginalStr, re.S)
            pageGroup.append(link)
        return pageGroup

    # 从html中解析我们需要的数据
    def getNeedInfo(self,sourceHtml):
        currentAllInfo = []
        selector = etree.HTML(sourceHtml)
        titles = selector.xpath('//dl[@class="blog_list clearfix"]//dd')
        singlePageInfo = {};
        for vs in titles:
            info = vs.xpath('h3[@class="tracking-ad"]/a/text()')
            print "标题:" + info[0]
            singlePageInfo['title'] = info[0]
            time = vs.xpath('div[@class="blog_list_b clearfix"]/div[@class="blog_list_b_r fr"]/label/text()')
            print "时间:" + time[0]
            singlePageInfo['time'] = time[0]
            readCount = vs.xpath('div[@class="blog_list_b clearfix"]/div[@class="blog_list_b_r fr"]/span/em/text()')
            print "阅读次数:" + readCount[0]
            currentAllInfo.append(singlePageInfo)
        print currentAllInfo


if __name__ == '__main__':
    spider = spider()
    url = "http://blog.csdn.net/?&page=1"
    allPage = spider.chagnePage(url)

    allPageInfo = []
    for link in allPage:
        print '正在处理：'+link
        sourceHtml = spider.getsource(link)
        spider.getNeedInfo(sourceHtml)