#教育机构 ：马士兵教育
#讲    师：杨淑娟
from  scrapy import  cmdline
#cmdline.execute('scrapy crawl douban'.split(' '))
#print('scrapy crawl douban'.split(' '))
cmdline.execute(['scrapy', 'crawl', 'douban'])