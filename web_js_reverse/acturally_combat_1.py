__author__ = 'ranshen0519@icloud.com'
import hashlib
import time
import requests
import base64
"""
https://spa6.scrape.center/
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
    # 3.将列表内容用逗号拼接；
    join = ','.join(api)
    # 4.将拼接的结果进行SHA1编码；
    sign = hashlib.sha1(join.encode()).hexdigest()
    # 5.将编码的结果和时间戳再次拼接；
    re_join = ','.join([sign, time_stamp])
    # 6.将拼接后的结果进行Base64编码。
    re_sign = base64.b64encode(re_join.encode())
    # 7.解码
    token_ = re_sign.decode()
    return token_


if __name__ == '__main__':
    # 1.将/api/movie放到一个列表里；
    api = ['/api/movie']
    token = get_token(api)
    for i in range(5):
        offset += (i * 10)
        real_ajax_url = ajax_url.format(limit, offset, token)
        # print(real_ajax_url)
        response = requests.get(real_ajax_url)
        print(response.json())
        time.sleep(1)
