# -*- coding: utf-8 -*-
import scrapy
from zhihuuser.items import ZhihuuserItem
from scrapy.http import Request
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20']

    def parse(self, response):
        result = json.loads(response.text)
        item = ZhihuuserItem()
        print item.fields
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        print item
