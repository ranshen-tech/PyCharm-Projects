__author__ = 'ranshen0519@icloud.com'
"""
利用 API 爬取数据
爬取电影《西游记之大圣归来》（地址 ），前 200 条 最新 短影评
http://movie.mtime.com/209164/
要求提取三个内容：
用户昵称；
影评内容；
评论对应的用户打分。
"""
import time
import requests


def get_movie_review(pages):
    url = 'http://front-gateway.mtime.com/library/movie/comment.api'
    params = {
        'tt': f'{int(time.time()) * 1000}',
        'movieId': '209164',
        'pageIndex': f'{pages}',
        'pageSize': '20',
        'orderType': '1'
    }
    headers = {
        'Referer': 'http://movie.mtime.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    res = requests.get(url, params, headers=headers)
    data_lst = res.json()['data']['list']
    for data in data_lst:
        nickname = data['nickname']
        content = data['content']
        rating = data['rating']
        print(f'用户昵称:{nickname}')
        print(f'影评内容:{content}')
        print(f'用户打分:{rating}\n')


def set_get_page(pages):
    for page in range(1, pages + 1):
        get_movie_review(pages)
        time.sleep(1)


set_get_page(10)
