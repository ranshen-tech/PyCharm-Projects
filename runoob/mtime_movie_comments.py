# __author__ = 'ranshen0519@icloud.com'
# import time
# import requests
#
#
# def get_data_lst(page):
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
#         'Referer': 'http://movie.mtime.com/'
#     }
#     params = {
#         'tt': f'{int(time.time()) * 100}',
#         'movieId': '251525',
#         'pageIndex': f'{page}',
#         'pageSize': '20',
#         'orderType': '1'
#     }
#     res = requests.get(
#         'http://front-gateway.mtime.com/library/movie/comment.api',
#         params=params,
#         headers=headers)
#     return res.json()['data']['list']
#
#
# def get_page_data(data_lst):
#     for info in data_lst:
#         comment = info['content']
#         nickname = info['nickname']
#         print(f'用户:{nickname}\n评论:{comment}')
#
#
# def set_page_num(pages):
#     for page in range(1, pages + 1):
#         get_page_data(get_data_lst(page))
#         time.sleep(1)
#
#
# set_page_num(5)


import time
import requests


def get_page_data(pages):
    url = 'http://front-gateway.mtime.com/library/movie/comment.api'
    params = {
        'tt': f'{int(time.time()) * 1000}',
        'movieId': '251525',
        'pageIndex': f'{pages}',
        'pageSize': '50',
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
        comment = data['content']
        print(f'用户昵称: {nickname}\n评论: {comment}')


def get_more_page(pages):
    for page in range(1, pages + 1):
        get_page_data(page)
        time.sleep(1)


# get_more_page(3)
get_page_data(1)
