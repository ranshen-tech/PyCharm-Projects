# __author__ = 'ranshen0519@icloud.com'
import requests


def simulate_login():
    url = 'https://wpblog.x0y1.com/wp-login.php'
    data = {
        'log': 'codetime',
        'pwd': 'shanbay520',
        'wp-submit': '登录',
        'redirect_to': 'https://wpblog.x0y1.com',
        'testcookie': '1'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    res = requests.post(url, data, headers=headers)
    # print(type(res.cookies))
    print(res.cookies)


simulate_login()


# import requests
# from bs4 import BeautifulSoup


# def get_data():
#     login_url = 'https://wpblog.x0y1.com/wp-login.php'
#     get_url = 'https://wpblog.x0y1.com'
#     get_params = {
#         'cat': '2'
#     }
#     login_data = {
#         'log': 'codetime',
#         'pwd': 'shanbay520',
#         'wp-submit': '登录',
#         'redirect_to': 'https://wpblog.x0y1.com',
#         'testcookie': '1'
#     }
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
#     }
#
#     login_res = requests.post(login_url, login_data, headers=headers)
#     shared_cookies = login_res.cookies  # important❗️
#     get_res = requests.get(get_url, get_params, headers=headers, cookies=shared_cookies)
#     soup = BeautifulSoup(get_res.text, 'html.parser')
#     titles = soup.select('h2.entry-title a')
    # for title in titles:
        # print(title.text, title.attrs)
        # print(title['href'])
    # link = [title['href'] for title in titles]
    # print(link)
    # link = [title.attrs['href'] for title in titles]
    # print(link)
    # content = soup.select('div.entry-content')
    # print(content[0])


# get_data()
