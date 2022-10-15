import urllib.request
import ssl

url = 'https://www.baidu.com'
resp = urllib.request.urlopen(url, context=ssl._create_unverified_context())
print(resp)
