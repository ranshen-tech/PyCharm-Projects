__author__ = 'ranshen0519@icloud.com'

import time

"""
1.将/api/movie放到一个列表里；
2.在列表中加入当前的时间戳；
3.将列表内容用逗号拼接；
4.将拼接的结果进行SHA1编码；
5.将编码的结果和时间戳再次拼接；
6.将拼接后的结果进行Base64编码。
需要借助两个库：一个是hashlib，他提供了sha1的方法；
另一个是base64库，他提供了b64encode方法对结果进行Base64编码
"""
ajax_url = 'https://spa6.scrape.center/api/movie/?limit={}&offset={}&token={}'
limit = 10
offset = 0


def get_token(args):
    # 2.在列表中加入当前的时间戳；
    time_stamp = str(int(time.time()))
    api.append(time_stamp)


if __name__ == '__main__':
    # 1.将/api/movie放到一个列表里；
    api = ['/api/movie']
