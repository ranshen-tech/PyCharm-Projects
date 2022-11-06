__author__ = 'ranshen0519@icloud.com'
import time
import requests
from bs4 import BeautifulSoup


def get_one_page(pages):
    url = 'https://movie.douban.com/top250'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    params = {'start': f'{pages * 25}'}  # 字符串字典格式
    print(params)
    res = requests.get(url, params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.select('div.hd > a')
    for link in links:
        name = link.select('span')[0].text
        print(f'{name}\t{link["href"]}')


for page in range(3):
    get_one_page(page)
    time.sleep(1)
