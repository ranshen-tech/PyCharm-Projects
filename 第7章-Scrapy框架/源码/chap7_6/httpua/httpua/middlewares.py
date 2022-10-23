# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


from  fake_useragent import  UserAgent
class HttpuaDownloaderMiddleware(object):


    def process_request(self, request, spider):
        request.headers['User-Agent']=UserAgent().random
        return None

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
