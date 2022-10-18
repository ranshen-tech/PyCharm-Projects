__author__ = 'ranshen0519@icloud.com'

# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup


# 将获取一页图书数据代码封装成函数 get_one_page_data()
def get_one_page_data():
    # 豆瓣读书 Top 250 首页 URL
    url = 'https://book.douban.com/250'
    # 定制消息头
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    # 根据传入参数定制查询参数
    params = {'start': 0}
    # 发送带消息头和查询参数的请求
    res = requests.get(url, headers=headers, params=params)
    # 解析成 BeautifulSoup 对象
    soup = BeautifulSoup(res.text, 'html.parser')
    # 提取出书名、作者、出版社信息并按行打印
    book_info_tags = soup.select('div.pl2 a')
    # soup = BeautifulSoup(res.text, 'html.parser')
    print(book_info_tags)


# 循环 10 次，分别获取第 1～10 页数据
get_one_page_data()
