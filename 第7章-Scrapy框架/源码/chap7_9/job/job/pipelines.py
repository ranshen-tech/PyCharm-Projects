# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from  pymongo import  MongoClient
class JobPipeline(object):
    def open_spider(self,spider):
        self.client=MongoClient()
        self.liepin=self.client.liepin.job

    def process_item(self, item, spider):
        self.liepin.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()
