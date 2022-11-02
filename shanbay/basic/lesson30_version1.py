__author__ = 'ranshen0519@icloud.com'

import time

from film_selector import FilmSelector
from seat_booking import SeatBooking


class Controller:
    def __init__(self, information):
        self.choice = None
        self.films = information  # 电影库所有电影
        self.welcome()
        self.choose_film()
        if self.choice != 'x':
            self.choose_seat()
        self.bye()

    def choose_film(self):
        selector = FilmSelector()
        selector.display_options(self.films)
        self.choice = selector.get_choice(self.films)

    def choose_seat(self):
        film = self.films[int(self.choice) - 1]
        name = film['name']
        symbol = film['symbol']
        seat_list = film['seats']
        booking = SeatBooking()
        booking.check_bookings(seat_list)
        booking.book_seat(seat_list)

    @staticmethod
    def welcome():
        print('+============================+')
        print('+     欢迎来到时光电影院     +')
        print('+============================+')
        print('')
        time.sleep(0.7)

    @staticmethod
    def bye(self):
        print('')
        time.sleep(0.2)
        print('+============================+')
        print('+  已经退出系统，下次见！👋  +')
        print('+============================+')

# seat_list = infos.infos[0]['seats']
# booking = SeatBooking()
# booking.check_bookings(seat_list)
# booking.book_seat(seat_list)
