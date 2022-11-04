__author__ = 'ranshen0519@icloud.com'
"""
所需解析的 HTML 代码，即响应的文本内容（res.text）；
用于解析 HTML 代码的 解析器，课程内使用的是 Python 内置解析器 html.parser（parser：解析器）
"""
# 导入 requests 库
# 从 bs4 库导入 BeautifulSoup

# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup

# 定制消息头
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

# 向 https://book.douban.com/top250/ 发送带消息头的请求
# 并将响应结果储存到 res 变量中
res = requests.get('https://book.douban.com/top250/', headers=headers)

# 将响应结果的文本内容解析为 BeautifulSoup 对象
# 并保存到变量 soup 中
soup = BeautifulSoup(res.text, 'html.parser')

# 所有书名所在元素
book_name_tags = soup.select('div.pl2 a')
# 所有书籍信息所在元素
book_info_tags = soup.select('p.pl')
# 遍历每本图书
for book_name_tag, book_info_tag in zip(book_name_tags, book_info_tags):
    # 通过元素 title 属性提取书名
    book_name = book_name_tag['title']
    # 获取书籍信息
    book_info = book_info_tag.text
    # 按“ / ”分割字符串
    book_info_list = book_info.split('/')
    # 结果列表中第一项为作者信息
    author = book_info_list[0]
    # 倒数第三项为出版社信息
    publisher = book_info_list[-3]
    # 打印书名、作者、出版社信息
    print(book_name, author, publisher)
