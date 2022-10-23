# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import  JobItem

class LiepinSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d+\.shtml.*'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'https://www.liepin.com/a/\d+\.shtml.*'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/zhaopin/.+curPage=\d+'),  follow=True),
    )

    def parse_item(self, response):

        title=response.css('.title-info h1::text').get() #职位的标题
        city=response.css('.basic-infor span a::text').get() #工作地点

        company= response.css('.company-logo p a::text').get() #公司名称
        job_qualifications=response.css('.job-qualifications span::text').getall() #任职资格
        job_desc_lst = response.css('.content.content-word::text').getall() #职位描述的列表
        job_desc=''.join(job_desc_lst).strip() #职位描述

        #yield
        item=JobItem(title=title,city=city,company=company,job_qualifications=job_qualifications,job_desc=job_desc)
        yield  item







