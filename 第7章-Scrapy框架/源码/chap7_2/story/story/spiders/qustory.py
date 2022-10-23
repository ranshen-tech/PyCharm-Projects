# -*- coding: utf-8 -*-
import scrapy

class QustorySpider(scrapy.Spider):
    name = 'qustory'
    allowed_domains = ['qu.la']
    start_urls = ['https://www.qu.la/book/118039/3540856.html']

    def parse(self, response):
        #解析提取数据
        title=response.xpath('//h1[@class="title"]/text()').extract()
        content=response.xpath('string(//div[@id="content"])').extract_first().strip().replace('　　','\n')
        next_url='https://www.qu.la/book'+response.xpath('//div[@class="section-opt"]/a.txt[3]/@href').extract_first()
        #print(next_url)
        yield {
            'title':title,
            'content':content
        }
        yield  scrapy.Request(next_url,callback=self.parse)
        #print(title,content)
        #pass

