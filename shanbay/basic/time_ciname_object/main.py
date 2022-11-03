# 2022.11.3 纪念！这个项目做的太爽了
from selector import Selector
from films import films
from booking import Booking


def welcome():
    print('欢迎来到时光电影院😃')


def bye():
    print('已经退出系统，下次见！👋')


def get_seat_lists(film_choice):
    return films[film_choice]['seats']


if __name__ == '__main__':
    welcome()
    select = Selector(films)
    if select.choice != 'x':
        select.choice = int(select.choice) - 1
        seat_lists = get_seat_lists(select.choice)
        booking = Booking(seat_lists)
    bye()
