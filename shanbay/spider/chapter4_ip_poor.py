__author__ = 'ranshen0519@icloud.com'

from random import choice

# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup


# 将获取一页图书数据代码封装成函数 get_one_page_data
def get_one_page_data(page, proxy):
    # 豆瓣读书 Top 250 首页 URL
    base_url = 'https://book.douban.com/top250/'
    # 定制消息头，内容省略
    headers = ...
    # 根据传入参数定制查询参数，内容省略
    params = ...
    # 发送带消息头、查询参数、代理的请求
    res = requests.get(
        base_url, headers=headers, params=params, proxies=proxy
    )
    # 解析成 BeautifulSoup 对象
    soup = BeautifulSoup(res.text, 'html.parser')
    # 提取出书名、作者、出版社信息并按行打印


# IP 代理池（瞎写的并没有用）
proxies_list = [
    {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    },
    {
        "http": "http://10.10.1.11:3128",
        "https": "http://10.10.1.11:1080",
    },
    {
        "http": "http://10.10.1.12:3128",
        "https": "http://10.10.1.12:1080",
    }
]
# 循环 10 次，分别获取第 1～10 页数据
for i in range(1, 11):
    # 从 IP 代理池中随机选择一个
    get_one_page_data(i, choice(proxies_list))
