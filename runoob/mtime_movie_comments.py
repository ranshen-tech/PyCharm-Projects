__author__ = 'ranshen0519@icloud.com'
import time
import requests


def get_data_lst(page):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Referer': 'http://movie.mtime.com/'
    }
    params = {
        'tt': f'{int(time.time()) * 100}',
        'movieId': '251525',
        'pageIndex': f'{page}',
        'pageSize': '20',
        'orderType': '1'
    }
    res = requests.get(
        'http://front-gateway.mtime.com/library/movie/comment.api',
        params=params,
        headers=headers)
    return res.json()['data']['list']


def get_page_data(data_lst):
    for info in data_lst:
        comment = info['content']
        nickname = info['nickname']
        print(f'用户:{nickname}\n评论:{comment}')


def set_page_num(pages):
    for page in range(1, pages + 1):
        get_page_data(get_data_lst(page))
        time.sleep(1)


set_page_num(5)
