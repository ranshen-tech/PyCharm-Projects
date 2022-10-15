# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.baidu.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }
# 发送请求
resp = urllib.request.urlopen(url)
html = resp.read().decode('gbk')  # decode将bytes类型转成str类型
print(html)
