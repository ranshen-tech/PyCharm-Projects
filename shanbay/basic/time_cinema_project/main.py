__author__ = 'ranshen0519@icloud.com'

import booking
import selector
import films

film, name, seats_list, symbol = None, None, None, None


def choose_film(films_):
    global film, name, seats_list, symbol
    selector.display_options(films_)
    choice = selector.get_choice(films_)
    film = films_[int(choice) - 1]
    name = film['name']
    seats_list = film['seats']
    symbol = film['symbol']


def choose_seat():
    print('正在为您预订电影《{}》的座位...'.format(name))
    print(symbol)
    print('支持的座位预订方式如下：')
    print("1 - 指定行列号预定座位")
    print("2 - 给我预订一个最靠前的座位！")
    method = input('请选择座位预订方式')
    valid_method = [str(i) for i in range(1, 3)]
    while method not in valid_method:
        method = input('没有按照要求输入哦，请重新输入')
    booking.check_bookings(seats_list)
    if method == '1':
        booking.book_seat(seats_list)
    else:
        booking.book_seat_at_front(seats_list)


def welcome():
    print('+      欢迎来到时光电影院       +')


def bye():
    print('+    已经退出系统，下次见！👋    +')


if __name__ == '__main__':
    welcome()
    choose_film(films.films)
    choose_seat()
    bye()
