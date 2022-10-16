# import requests
#
# url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
# resp = requests.get(url)
#
# # 存储
# with open('logo.png', 'wb') as file:
#     file.write(resp.content)


import requests

url = 'https://www.baidu.com/img/pc_675fe66eab33abff35a2669768c43d95.png'
resp = requests.get(url)
# store
with open('logo.png', 'wb') as f:
    f.write(resp.content)
