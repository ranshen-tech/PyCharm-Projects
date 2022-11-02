__author__ = 'ranshen0519@icloud.com'
from infos import infos
from film_selector import FilmSelector
from seat_booking import SeatBooking


class Controller:
    def __init__(self, information):
        self.films = information  # 电影库所有电影
        self.welcome()
        self.choose_film()
        if self.choice != 'x':
            self.choose_seat()
        self.bye()

    def choose_film(self):
        selector = FilmSelector()
        selector.display_options(self.films)
        selector.get_choice(self.films)

    def choose_seat(self):
        booking = SeatBooking()
        booking.check_bookings()
        booking.book_seat()

    def welcome(self):
        pass

    def bye(self):
        pass


# seat_list = infos.infos[0]['seats']
# booking = SeatBooking()
# booking.check_bookings(seat_list)
# booking.book_seat(seat_list)
