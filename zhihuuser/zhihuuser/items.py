# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuuserItem(scrapy.Item):
    name = scrapy.Field()
    user_type = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    headline = scrapy.Field()
    articles_count = scrapy.Field()
    gender = scrapy.Field()
    vip_info = scrapy.Field()
    is_advertiser = scrapy.Field()
    avatar_url = scrapy.Field()
    is_org = scrapy.Field()
    follower_count = scrapy.Field()
