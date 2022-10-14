# from urllib.request import urlopen
#
#
# url = "https://www.baidu.com"
# resp = urlopen(url)
#
# print(resp)


# import requests
#
# url = "https://www.baidu.com"
# res = requests.get(url)
# res.encoding = "utf-8"
# with open('baidu.html', 'wb') as f:
#     f.write(res.content)

import urllib.request

url = 'https://www.douban.com'
webPage = urllib.request.urlopen(url)
print(webPage)
data = webPage.read()
print(data)
print(data.decode('utf-8'))
