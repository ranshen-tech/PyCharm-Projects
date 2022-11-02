__author__ = 'ranshen0519@icloud.com'
import time


class FilmSelector:
    # 展示所有可选项
    @staticmethod
    def display_options(films):
        print("今日影院排片列表：")
        print('+================+')
        FilmSelector.display_films(films)
        print('x - 退出')
        print('+================+')
        time.sleep(0.7)
    # 获取用户的选择

    def get_choice(self):
        pass

    @staticmethod
    def display_films(films):
        for i in range(len(films)):
            print(f'{i+1} - {films[i]["name"]}')
            time.sleep(0.1)
