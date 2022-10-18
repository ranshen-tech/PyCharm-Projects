__author__ = 'ranshen0519@icloud.com'
import requests
from bs4 import BeautifulSoup
import time


def get_one_page_data(page):
    # 豆瓣读书 Top 250 首页 URL
    url = 'https://book.douban.com/top250'
    # 定制消息头
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    # 根据传入参数定制查询参数
    params = {'start': page * 25}
    # 发送带消息头和查询参数的请求
    res = requests.get(url, headers=headers, params=params)
    # 解析成 BeautifulSoup 对象
    soup = BeautifulSoup(res.text, 'html.parser')
    # 提取出书名、作者、出版社信息并按行打印
    book_name_tags = soup.select('div.pl2 a')
    book_info_tags = soup.select('p.pl')
    for book_name_tag, book_info_tag in zip(book_name_tags, book_info_tags):
        book_name = book_name_tag['title']
        author = book_info_tag.text.split(' / ')[0]
        publisher = book_info_tag.text.split(' / ')[-3]
        print(f'{book_name}\n{author}\n{publisher}\n{"-"*20}')
        # print(book_name_tag['title'])
    # print(type(book_info_tags[0].text))


# 循环 10 次，分别获取第 1～10 页数据
for i in range(10):
    get_one_page_data(i)
    time.sleep(1)
