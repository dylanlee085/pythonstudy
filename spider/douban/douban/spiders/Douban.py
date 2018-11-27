# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urlparse import urljoin
from douban.items import DoubanItem

# way1
class DoubanSpider(scrapy.Spider):
    name = 'Douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250',
                ]
    def parse(self, response):
        books = response.xpath('//div[@id="wrapper"]/div[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/div[@class="indent"]/table[@width="100%"]')
        for each_book in books:
            item = DoubanItem()
            item['name'] = each_book.xpath('normalize-space(./tr/td/div[@class="pl2"]/a/text())').extract()[0]
            item['url'] = each_book.xpath('./tr/td/div[@class="pl2"]/a/@href').extract()[0]
            yield item
        nextLink = response.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)


#way2
# class DoubanSpider(scrapy.Spider):
#     name = 'Douban'
#     allowed_domains = ['douban.com']
#     start_urls = ['https://book.douban.com/top250?start=0',
#                   'https://book.douban.com/top250?start=25',
#                   'https://book.douban.com/top250?start=50',
#                   'https://book.douban.com/top250?start=75',
#                   'https://book.douban.com/top250?start=100',
#                   'https://book.douban.com/top250?start=125',
#                   'https://book.douban.com/top250?start=150',
#                   'https://book.douban.com/top250?start=175',
#                   'https://book.douban.com/top250?start=200',
#                   'https://book.douban.com/top250?start=225']
#     def parse(self, response):
#         books = response.xpath('//div[@id="wrapper"]/div[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/div[@class="indent"]/table[@width="100%"]')
#         for each_book in books:
#             item = DoubanItem()
#             item['name'] = each_book.xpath('normalize-space(./tr/td/div[@class="pl2"]/a/text())').extract()[0]
#             item['url'] = each_book.xpath('./tr/td/div[@class="pl2"]/a/@href').extract()[0]
#             yield item
