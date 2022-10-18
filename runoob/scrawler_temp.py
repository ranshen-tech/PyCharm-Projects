__author__ = 'ranshen0519@icloud.com'
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
url_ = 'https://movie.douban.com/top250'


def get_data(url, user_agent):
    res = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.select('div.hd a')

    # print(movie_tags[0].select('span.title')[0].text, end='')
    # print(movie_tags[0].text.split('/')[0])


def process_data(datas):
    for data in datas:
        movie_name = data.text.split('/')[0]
        movie_link = data['href']
        print(movie_name.strip(), movie_link)
        # print(type(movie_name.strip()), type(movie_link))


movie_tags = get_data(url_, headers)
process_data(movie_tags)
