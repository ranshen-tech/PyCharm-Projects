__author__ = 'ranshen0519@icloud.com'

# 导入 SeatBooking 类和 infos 列表
import seat_booking
import infos
import film_selector

selector = film_selector.FilmSelector()
# selector.display_films(infos.infos)
selector.display_options(infos.infos)
seat_list = infos.infos[0]['seats']
booking = seat_booking.SeatBooking()
booking.check_bookings(seat_list)
booking.book_seat(seat_list)
