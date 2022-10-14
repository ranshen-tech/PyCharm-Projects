import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数:封装到字典中
    kw = input('enter the word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    # step3
    page_text = response.text
    # step4
    filename = f'{kw}.html'
    with open(filename, 'w') as f:
        f.write(page_text)
    print(f'{filename}保存成功！')
