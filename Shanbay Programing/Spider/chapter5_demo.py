__author__ = 'ranshen0519@icloud.com'
import time
import requests


for page in range(1, 4):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'referer': 'http://movie.mtime.com/'
    }

    params = {
        # 将当前时间戳转为毫秒后取整，作为 tt 的值
        "tt": "{}".format(int(time.time() * 1000)),
        "movieId": "251525",
        "pageIndex": f"{page}",
        "pageSize": "50",
        "orderType": "1"
    }

    res = requests.get('http://front-gateway.mtime.com/library/movie/comment.api', params, headers=headers)
    comment_list = res.json()['data']['list']
    for i in comment_list:
        print('用户: ', i['nickname'])
        print('评论: ', i['content'])
    time.sleep(1)
