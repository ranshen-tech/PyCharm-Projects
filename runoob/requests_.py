__author__ = 'ranshen0519@icloud.com'
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

# res = requests.get('https://book.douban.com/top250', headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(type(res.text))

# book_name_taps = soup.select('div.pl2 a')
# print(book_name_taps)
# print(type(book_name_taps[0]))
# book = book_name_taps[0]
# print(book['title'])
# book_info_tags = soup.select('p.pl')


# url_ = input('Please enter request URL: ')
user_agent_ = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
url_ = 'https://book.douban.com/top250'


def get_data(url, user_agent):
    # step1.发送请求，并将结果存储到res变量
    res = requests.get(url, headers=user_agent)
    # step2.将响应结果的文本内容解析为BeautifulSoup对象，并将结果存储到soup变量中
    soup = BeautifulSoup(res.text, 'html.parser')
    # step3.To process
    book_name_tags = soup.select('div.pl2 a')
    book_info_tags = soup.select('p.pl')
    for book_name_tag, book_info_tag in zip(book_name_tags, book_info_tags):
        # 通过元素title属性提取书名
        book_name = book_name_tag['title']
        # 获取书籍信息
        book_info = book_info_tag.text
        # 按'/'分隔字符串
        book_info_list = book_info.split('/')
        author = book_info_list[0]
        publisher = book_info_list[-3]
        print(f'{book_name} {author}{publisher}')


get_data(url_, user_agent_)
