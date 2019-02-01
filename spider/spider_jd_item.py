#! /usr/bin/env python
# coding: utf-8


#! /usr/bin/env python
# coding: utf-8


'''
1.获取淘宝联盟数据
2.将联盟数据插入数据库
3.分析数据库中高佣金率的品类
'''


import requests
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
# from bs4 import BeautifulSoup
import spider_jd
from lxml import etree


def get_html():
    cookie = 'shshshfpa=cef7802c-97a5-3a76-ada2-825e9a159bfe-1538187456; shshshfpb=1295cdb85bb3a461295dfb60f777748905da71b4c84c3b9135baee0c07; o2Control=webp; __jdu=2002110157; PCSYCityID=1601; ipLoc-djd=1-72-4137-0; areaId=1; _gcl_au=1.1.54286832.1539074688; 3AB9D23F7A4B3C9B=F7FESRYU5RNEQZHWWW5BBDOBORL5WBD5AOSIF4563KS6UKKV4T4UDQF3EO4F5NID47QYAYM73OURLGTFQ4HHS2RZ7I; __jda=122270672.2002110157.1537179742.1539074680.1539674641.2; __jdc=122270672; __jdv=122270672|direct|-|none|-|1539674641334; shshshfp=7e6b5859da73f076336954f094df67ac; user-key=ac30a911-4af7-4287-b4ad-abd462050369; cn=0; shshshsID=987cbe9536496173ef87c58d2edee389_4_1539675765884; __jdb=122270672.19.2002110157|2.1539674641'
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Cookie': cookie}
    for value in spider_jd.main():
        category_url = value[1]
        category = value[0]
        print category_url, category
        if 'cat=' in category_url:
            response = requests.get(category_url, headers)
            html = response.text
            yield  html


def parse_html(html):
    # soup = BeautifulSoup(html, 'html.parser')
    # content = soup.findAll('ul', class_='gl-warp clearfix')
    # for ul in content:
    #     lis = ul.findAll('li')
    #     for li in lis:
    #         item_url = ['https:' + a.attrs['href'] for a in li.findAll('div', class_='p-name' or 'p-name p-name-type3')[0].findAll('a')][0]
    #         item_name = [em.string for em in li.findAll('div', class_='p-name')[0].findAll('a')[0].findAll('em')][0].lstrip()
    #         print item_url
    #         print item_name
    #         print '====================================================================================================================='
    selector = etree.HTML(html)
    items = selector.xpath('//li[@class="gl-item"]')
    for i in range(0, len(items)):
        url = selector.xpath('//div[@class="p-img"]/a')[i].get('href').split('//')[1]
        print url
        try:
            img = selector.xpath('//div[@class="p-img"]/a/img')[i].get('src').split('//')[1]
            print img
        except Exception as e:
            img = selector.xpath('//div[@class="p-img"]/a/img')[i].get('data-lazy-img').split('//')[1]
            print img
        try:
            price = selector.xpath('//div[@class="p-price"]/strong/i//text()')[i]
            print price
        except Exception as e:
            price = 'null'
            print price
        try:
            title = selector.xpath('//div[@class="p-img"]/a')[i].get('title')
            print title
        except Exception as e:
            print 'null'

if __name__ == '__main__':
    # html = get_html()
    # parse_html(html)
    for i in get_html():
        parse_html(i)
        break



