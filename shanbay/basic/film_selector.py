__author__ = 'ranshen0519@icloud.com'
import time


class FilmSelector:
    # 展示所有可选项
    def display_options(self):
        pass

    # 获取用户的选择
    def get_choice(self):
        pass

    @staticmethod
    def display_films(films):
        for i in range(len(films)):
            print(films[i]['name'])
            time.sleep(0.1)
