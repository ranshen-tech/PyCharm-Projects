# import requests
#
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn=240&rn=30&gsm=f0&1592041096731='
# resp = requests.get(url)
# json_data = resp.json()
# print(json_data)


import requests

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8162291105978265078&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a0000000000005a&1665830636963='
resp = requests.get(url)
json_data = resp.json()
print(json_data)
