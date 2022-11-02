__author__ = 'ranshen0519@icloud.com'

# 导入 SeatBooking 类和 infos 列表
import seat_booking
import infos
# 从 infos 列表中取出第一部电影的座位表
seat_list = infos.infos[0]['seats']
# 实例化 SeatBooking 类
booking = seat_booking.SeatBooking()
# 打印所有座位的预订信息
booking.check_bookings(seat_list)
# 按用户输入的座位号预订座位
booking.book_seat(seat_list)
