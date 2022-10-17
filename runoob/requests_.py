__author__ = 'ranshen0519@icloud.com'
# step1
import requests
# step2
from bs4 import BeautifulSoup
# step3
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# step4
res = requests.get('https://book.douban.com/top250', headers=headers)
# step5
soup = BeautifulSoup(res.text, 'html.parser')
# print(type(soup))
# step6
book_name_taps = soup.select('div.pl2 a')
# print(book_name_taps[0])
# print(type(book_name_taps[0]))
# book = book_name_taps[0]
# print(book['title'])
# step7
book_info_tags = soup.select('p.pl')
# print(book_info_tags)
for info_tag in book_info_tags:  # 遍历所有书籍信息元素
    info = info_tag.text  # 获取书籍信息
    info_list = info.split()
