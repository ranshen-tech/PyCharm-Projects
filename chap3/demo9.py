# 教育机构 ：马士兵教育
# 讲    师：杨淑娟

import urllib.error
import urllib.request
import ssl
context = ssl._create_unverified_context()

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://movie.douban.com/'
try:
    resp = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print('原因:', e.reason)
    print('响应状态码:', str(e.code))
    print('响应头数据:', e.headers)
