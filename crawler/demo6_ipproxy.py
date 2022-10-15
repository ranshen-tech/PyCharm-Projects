# 教育机构 ：马士兵教育
# 讲    师：杨淑娟

from urllib.request import ProxyHandler
from urllib.request import build_opener

proxy = ProxyHandler({'http': '60.2.44.182:30963'})

opener = build_opener(proxy)

url = 'https://www.xslou.com/'
resp = opener.open(url)
print(resp.read().decode('gbk'))
