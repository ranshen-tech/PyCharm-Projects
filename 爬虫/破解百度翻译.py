import requests
import json

if __name__ == '__main__':
    # step1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # step2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    # step3.post请求参数处理(同get请求一致)
    data = {
        'kw': 'dog'
    }
    # step4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # step5.获取响应数据（确认响应数据是json类型，使用json方法返回字典对象）
    dict_obj = response.json()
    print(dict_obj)
    # step6.持久化存储
    fp = open('dog.json', 'w')
    json.dump(dict_obj, fp=fp)

