# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals



from scrapy.http import  HtmlResponse
from selenium.webdriver import  Chrome
class SsDownloaderMiddleware(object):
    # def __init__(self):
    #     self.driver=Chrome()

    def process_request(self, request, spider):
        spider.driver.get(request.url)
        html=spider.driver.page_source

        return  HtmlResponse(url=request.url,request=request,body=html,encoding='utf-8')

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a.txt Response object
        # - return a.txt Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a.txt download handler or a.txt process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a.txt Response object: stops process_exception() chain
        # - return a.txt Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
