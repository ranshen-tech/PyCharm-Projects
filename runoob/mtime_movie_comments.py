__author__ = 'ranshen0519@icloud.com'

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Referer': 'http://movie.mtime.com/'
}

res = requests.get('http://front-gateway.mtime.com/library/movie/comment.api?tt=1666154717907&movieId=251525&pageIndex=1&pageSize=20&orderType=1', headers=headers)
print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# comments = soup.select('ul.list > li > div.contentBox > p.content')
# print(comments)
# for comment in comments:
#     print(comment.text)
