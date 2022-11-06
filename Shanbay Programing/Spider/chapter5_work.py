__author__ = 'ranshen0519@icloud.com'
"""
利用 API 爬取数据，爬取电影《西游记之大圣归来》http://movie.mtime.com/209164/，前 200 条 最新 短影评

要求提取三个内容：
用户昵称；
影评内容；
评论对应的用户打分。
"""
import requests
import time
url = 'http://front-gateway.mtime.com/library/movie/comment.api'

for i in range(1, 6):
    payload = {
        'tt': f'{int(time.time()) * 1000}',
        'movieId': '209164',
        'pageIndex': f'{i}',
        'pageSize': '40',
        'orderType': '2'
    }

    headers = {
        'Referer': 'http://movie.mtime.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    r = requests.get(url, payload, headers=headers)
    reviews = r.json()['data']['list']
    for review in reviews:
        print(f'用户昵称: {review["nickname"]}')
        print(f'影评内容: {review["content"]}')
        print(f'用户打分: {review["rating"]}')
    time.sleep(1)
