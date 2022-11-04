__author__ = 'ranshen0519@icloud.com'


class Selector:
    def __init__(self, films_):
        self.display_options(films_)
        self.choice = self.get_choice(films_)
        self.film_lists = self.get_film_lists(films_)

    def __str__(self):
        return '电影选择'

    @staticmethod
    def display_options(films_):
        print("今日影院排片列表：")
        for i in range(len(films_)):
            print(f'{i + 1} - {films_[i]["name"]}')
        print('x - 退出')

    @staticmethod
    def get_choice(films_):
        valid_choice = [str(i + 1) for i in range(len(films_))]
        valid_choice.append('x')
        choice = input('你的选择是？')
        while choice not in valid_choice:
            choice = input('没有按照要求输入哦，请重新输入 ')
        return choice

    def get_film_lists(self, films_):
        if self.choice != 'x':
            return films_[int(self.choice) - 1]['seats']

