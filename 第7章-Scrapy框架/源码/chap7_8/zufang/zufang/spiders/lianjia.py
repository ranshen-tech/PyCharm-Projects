# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://bj.lianjia.com/zufang/pg{i}/#contentList' for i in range(1,3)]

    def parse(self, response):
       full_url=['https://bj.lianjia.com'+url for url in  response.xpath('//div[@class="content__list--item--main"]/p[1]/a.txt/@href').extract()]

       for item in full_url:

           yield scrapy.Request(url=item,callback=self.parse_info)

    def parse_info(self,response):

        title=response.xpath('//div[@class="content clear w1150"]/p/text()').get() #房源的标题
        total_price=response.xpath('//div[@class="content__aside--title"]/span/text()|//div[@class="content__aside--title"]/text()').extract()
        price=''.join(total_price).strip(' ').replace('\n            ','').replace('            \n','') #价格
        mode=response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get() #租赁方式
        type=response.xpath('//ul[@class="content__aside__list"]/li[2]//text()').get() #房屋类型：
        direction=response.xpath('//ul[@class="content__aside__list"]/li[3]//text()').get() #楼层信息
        elevator=response.xpath('//div[@class="content__article__info"]/ul/li[9]/text()').get() #电梯
        parking=response.xpath('//div[@class="content__article__info"]/ul/li[11]/text()').get() #车位
        water=response.xpath('//div[@class="content__article__info"]/ul/li[12]/text()').get()# 用水
        electric=response.xpath('//div[@class="content__article__info"]/ul/li[14]/text()').get() #用电
        heating=response.xpath('//div[@class="content__article__info"]/ul/li[15]/text()').get() #燃气情况

        yield {
            'title':title,
            'price':price,
            'mode':mode,
            'type':type,
            'direction':direction,
            'elevator':elevator,
            'parking':parking,
            'water':water,
            'electric':electric,
            'heating':heating
        }





