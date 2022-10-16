# import requests
#
# url = 'https://www.so.com/s'
# params = {'q': 'python'}
# resp = requests.get(url, params=params)
# resp.encoding = 'utf-8'
# print(resp.text)


import requests

url = 'https://so.com/s'
params = {'q': 'python'}
resp = requests.get(url, params=params)
print(resp.encoding)
print(resp.text)
