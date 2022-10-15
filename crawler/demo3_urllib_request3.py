# import urllib.request
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# url = 'https://movie.douban.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
#
# # 构建请求对象
# req = urllib.request.Request(url, headers=headers)
#
# # 使用urlopen打开请求
# resp = urllib.request.urlopen(req)
#
# # 从响应结果中读取数据
# html = resp.read().decode('utf-8')
# print(html)


import urllib.request
import ssl

url = 'https://movie.douban.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'}
# 构建请求对象
req = urllib.request.Request(url, headers=headers)
# 使用urlopen打开请求
resp = urllib.request.urlopen(req, context=ssl._create_unverified_context())
# 从响应结果中读取数据
html = resp.read().decode()
print(html)
