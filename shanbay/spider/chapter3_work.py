__author__ = 'ranshen0519@icloud.com'
import requests
from bs4 import BeautifulSoup
# 电影名和链接
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

res = requests.get('https://movie.douban.com/top250', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# print(type(soup))
links = soup.select('div.hd > a')
for link in links:
    name = link.select('span')[0]
    print(name.text, link['href'])
