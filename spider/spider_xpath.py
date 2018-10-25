#! /usr/bin/env python
# coding: utf-8

#读取字符串
# from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result)

#读取文本
# from lxml import etree
# html = etree.parse('hello.html')
# result = etree.tostring(html, pretty_print=True)
# print result

#读取标签
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li')
# print result
# print type(result)
# print result[0]

#读取标签的class
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li/@class')
# print result

#读取标签li下hre为link1.html的<a>标签
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li/a[@href="link1.html"]')
# print result

#读取标签li下的所有span标签
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li//span')
# print result

#获取li标签下的所有class，但不包括li
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li/a//@class')
# print result

#获得最后一个li的<a>的href
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li[last()]/a/@href')
# print result


#获得倒数第二个li的<a>的href
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//li[last() -1]/a')
# print result[0].text

#获取class为bold的签名
# from lxml import etree
# html = etree.parse('hello.html')
# result = html.xpath('//*[@class="bold"]')
# print result[0].tag

import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_html(url):
    print 'starting get_html......'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    return html

def parse_html(html):
    print 'starting parse_html......'
    html = etree.HTML(html)
    result = html.xpath('//li/text()|//p/text()')
    print 'staring write_file......'
    for i in result:
        with open('webfile.txt', 'a') as f:
            f.write(i)

if __name__ == "__main__":
    url = 'https://juejin.im/post/5baed64c5188255c4834c132?utm_source=gold_browser_extension'
    html = get_html(url)
    parse_html(html)














