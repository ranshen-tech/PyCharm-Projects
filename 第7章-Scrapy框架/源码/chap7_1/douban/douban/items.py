# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    publish=scrapy.Field()
    score=scrapy.Field()

#测试
'''book=DoubanItem()
book['title']='红楼梦'
book['publish']='[清] 曹雪芹 著 / 人民文学出版社 / 1996-12 / 59.70元'
book['score']='9.6'
print(book)
print(type(book))'''
