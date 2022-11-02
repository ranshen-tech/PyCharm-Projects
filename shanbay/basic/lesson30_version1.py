__author__ = 'ranshen0519@icloud.com'

# 导入 SeatBooking 类和 infos 列表
import seat_booking
import infos
import film_selector


class Controller:
    def __init__(self, information):
        self.films = information  # 电影库所有电影
        self.welcome()
        self.choose_film()
        if self.choice != 'x':
            self.choose_seat()
        self.bye()

    def choose_film(self):
        pass

    def choose_seat(self):
        pass

    def welcome(self):
        pass

    def bye(self):
        pass


selector = film_selector.FilmSelector()
# selector.display_films(infos.infos)
selector.display_options(infos.infos)
seat_list = infos.infos[0]['seats']
booking = seat_booking.SeatBooking()
booking.check_bookings(seat_list)
booking.book_seat(seat_list)
