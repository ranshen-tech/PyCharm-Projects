# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print('--------------------------------------------')
        print(response.text)
        print('--------------------------------------------')
        yield  scrapy.Request(self.start_urls[0],dont_filter=True)
