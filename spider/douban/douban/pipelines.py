# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def process_item(self, item, spider):
        with open("book.txt", 'a') as f:
            f.write(item['name'].encode("utf8") + ' ' + item['url'].encode("utf8") + '\n')
