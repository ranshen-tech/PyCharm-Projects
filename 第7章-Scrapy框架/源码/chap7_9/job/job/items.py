# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    title=scrapy.Field()
    city=scrapy.Field()
    company=scrapy.Field()
    job_qualifications=scrapy.Field()
    job_desc=scrapy.Field()
