import ssl
import urllib.request
# ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://www.baidu.com/'
# 发送请求
response = urllib.request.urlopen(url, context=ssl._create_unverified_context())
html = response.read().decode('gbk')  # decode将bytes类型转成str类型
print(html)
