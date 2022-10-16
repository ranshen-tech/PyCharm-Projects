# import requests
# from lxml import etree
#
# url = 'https://www.qidian.com/rank/yuepiao'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
#
# # 发送请求
# resp = requests.get(url, headers)
# e = etree.HTML(resp.text)  # 类型转换 将str类型转换成class 'lxml.etree._Element'
# # print(type(e))
# names = e.xpath('//div[@class="book-mid-info"]/h4/a/text()')
# authors = e.xpath('//p[@class="author"]/a[1]/text()')
# # print(names)
# # print(authors)
# for name, author in zip(names, authors):
#     print(name, ":", author)


# //div[@class="book-mid-info"]/h2/a/text()
# //p[@class="author"]/a
import requests
from lxml import etree

url = 'https://www.qidian.com/rank/yuepiao/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
resp = requests.get(url, headers=headers)
etree = etree.HTML(resp.text)  # 类型转换 将str类型转换成etree类型，这样才能使用etree类的方法
print(type(etree))
fiction_names = etree.xpath('//div[@class="book-mid-info"]/h2/a/text()')
# print(fiction_names)
authors = etree.xpath('//p[@class="author"]/a/text()')
# print(authors)
for name, author in zip(fiction_names, authors):
    print(f'{name}: {author}')
