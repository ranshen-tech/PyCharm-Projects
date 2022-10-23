# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from  pymongo import  MongoClient
class ZufangPipeline(object):
    def open_spider(self, spider):
        self.client=MongoClient()
        self.lianjia=self.client.zufang.lianjia

    def process_item(self, item, spider):
        self.lianjia.insert(dict(item))

    def close_spider(self, spider):
        self.client.close()
