__author__ = 'ranshen0519@icloud.com'
import requests
from bs4 import BeautifulSoup
import time


def get_page_data(pages):
    url = 'https://movie.douban.com/top250'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    params = {'start': pages * 25}
    res = requests.get(url, params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # movie_info_tags = soup.select('div.hd a')
    movie_info_tags = soup.select('div.bd > p')
    print(movie_info_tags)
    # print(movie_name_tags[0].select('span.title')[0].text)
    # print(movie_name_tags[0].text.split('/')[0].strip())
    # for movie_info_tag in movie_info_tags:
    #     movie_name_tag = movie_info_tag.select('span.title')[0].text
    #     movie_link_tag = movie_info_tag['href']
    #     print(movie_name_tag, movie_link_tag)
    # print(movie_info_tags[0])
    # print(type(movie_info_tags))


def get_more_page(pages):
    for page in range(pages):
        get_page_data(page)
        time.sleep(1)


get_page_data(0)
# get_more_page(10)
