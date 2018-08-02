#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import lxml.html
import time
from lxml.cssselect import CSSSelector
from MongoCache import MongoCache
import threading


def download(url,num_retries=2):
    """下载整个页面"""
    print 'Downloading:', url

    # 设置用户代理
    user_agent = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:', e.reason
        html = None

        # 只有在服务器报500-600错误时，才会重试下载，仅重试2次
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html


def get_data(url):
    """从详细页面 获取各字段数据"""

    #  如果缓存中有该页面数据，则直接获取使用；否则，先下载页面，再使用
    cache = MongoCache()
    if not cache.__getitem__(url):
        html_text_detail = download(url)
        if not html_text_detail:
            print 'None:', url
        else:
            cache.__setitem__(url, html_text_detail)
    else:
        print 'Exists:', url
        html_text_detail = cache.__getitem__(url)

    try:
        #  获取个字段数据
        tree = lxml.html.fromstring(html_text_detail)

        house_title = CSSSelector('div.main-wrap > div.house-title > h1')
        house_pay_way1 = CSSSelector('div.house-pay-way > span:nth-child(1)')
        house_pay_way2 = CSSSelector('div.house-pay-way > span:nth-child(2)')
        print house_title(tree)[0].text_content()
        print '%s|%s' % (house_pay_way1(tree)[0].text_content(), house_pay_way2(tree)[0].text_content())

        for i in range(7):
            for j in range(2):
                css = 'div.house-desc-item > ul.f14 > li:nth-child(%s) > span:nth-child(%s)' % (i+1, j+1)
                house_info = CSSSelector(css)
                print house_info(tree)[0].text_content().replace(' ', '')

    except TypeError as e:
        print 'HTML文本发生错误：%s' % e
    except IndexError as e:
        print '获取详细数据发生错误：%s' % e


def get_url(html):
    """获取需爬取数据的链接集"""
    tree = lxml.html.fromstring(html)
    sel = CSSSelector('div.mainbox > div.main > div.content > div.listBox > ul.listUl > li > div.des > h2 > a')
    url_list = []
    for i in sel(tree):
        if i.get('href') not in url_list:
            url_list.append(i.get('href'))
    return url_list


if __name__ == '__main__':
    url_index = 'http://bj.58.com/chuzu/'
    html_text_list = download(url_index)
    url_list = get_url(html_text_list)

    for url_detail in url_list:
        thr = threading.Thread(target=get_data, args=(url_detail,))
        thr.start()
        print '-------------------Thread Name: %s----------------' % thr.getName()
        time.sleep(2)  # 延时2s,如果注释这代码，运行会很快结束。
