# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class StoryPipeline(object):
    def open_spider(self, spider):
        self.file=open('story.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        info=''.join(item['title'])+"\t"+item['content']+"\n"
        self.file.write(info)
        #print(item['title'])
        return item

    def close_spider(self, spider):
        self.file.close()