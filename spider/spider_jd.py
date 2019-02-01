#! /usr/bin/env python
# coding: utf-8


'''
1.获取淘宝联盟数据
2.将联盟数据插入数据库
3.分析数据库中高佣金率的品类
'''


import requests
#import xproxy
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
from bs4 import BeautifulSoup

def get_html():
    url = 'https://www.jd.com/allSort.aspx'
    cookie = 'shshshfpa=cef7802c-97a5-3a76-ada2-825e9a159bfe-1538187456; shshshfpb=1295cdb85bb3a461295dfb60f777748905da71b4c84c3b9135baee0c07; o2Control=webp; __jdu=2002110157; PCSYCityID=1601; ipLoc-djd=1-72-4137-0; areaId=1; _gcl_au=1.1.54286832.1539074688; 3AB9D23F7A4B3C9B=F7FESRYU5RNEQZHWWW5BBDOBORL5WBD5AOSIF4563KS6UKKV4T4UDQF3EO4F5NID47QYAYM73OURLGTFQ4HHS2RZ7I; __jda=122270672.2002110157.1537179742.1539074680.1539674641.2; __jdc=122270672; __jdv=122270672|direct|-|none|-|1539674641334; shshshfp=7e6b5859da73f076336954f094df67ac; user-key=ac30a911-4af7-4287-b4ad-abd462050369; cn=0; shshshsID=987cbe9536496173ef87c58d2edee389_4_1539675765884; __jdb=122270672.19.2002110157|2.1539674641'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Cookie': cookie}
    response = requests.get(url, headers)
    html = response.text
    return html


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.findAll('dl', class_='clearfix')
    for dl in content:
        # dts = dl.findAll('dt')
        # for dt in dts:
        #     print '================================================================================'
        #     categorys_url = 'https:' + dt.a.attrs['href']
        #     categorys = dt.a.string
 #           print '当前品类为%s, %s' % (categorys, categorys_url)
        for dds in dl.findAll('dd'):
            for dd in dds.findAll('a'):
                category_url = 'https:' + dd.attrs['href']
                category = dd.string
                yield category,category_url

def main():
    html = get_html()
    parse_html(html)
    category_url = []
    for i in parse_html(html):
        category_url.append(i)
    return category_url



if __name__ == '__main__':
    main()
