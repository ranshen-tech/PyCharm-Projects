__author__ = 'ranshen0519@icloud.com'


def display_options(films_):
    print("今日影院排片列表：")
    for i in range(len(films_)):
        print(f'{i + 1} - {films_[i]["name"]}')
    print('x - 退出')


def get_choice(films_):
    valid_choice = [str(i + 1) for i in range(len(films_))]
    valid_choice.append('x')
    choice = input('你的选择是？')
    while choice not in valid_choice:
        choice = input('没有按照要求输入哦，请重新输入 ')
    return choice
