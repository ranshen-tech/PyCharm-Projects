import time


class FilmSelector:
    # 展示所有可选项
    @staticmethod
    def display_options(films):
        print("今日影院排片列表：")
        print('+================+')
        for i in range(len(films)):
            print(f'{i + 1} - {films[i]["name"]}')
            time.sleep(0.2)
        print('x - 退出')
        print('+================+')
        time.sleep(0.7)

    @staticmethod
    def get_choice(films):
        valid_choice = [i + 1 for i in range(len(films))]
        valid_choice.append('x')
        choice = int(input('你的选择是？ '))
        while choice not in valid_choice:
            choice = int(input('没有按照要求输入哦，请重新输入 '))
        return choice
