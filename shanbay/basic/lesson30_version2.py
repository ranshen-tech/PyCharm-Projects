from film_selector import FilmSelector
from infos import infos
from seat_booking import SeatBooking


class Controller:
    def __init__(self, infos):
        self.films = infos  # 电影库所有电影
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
        seats_list = film['seats']
        symbol = film['symbol']

        # 打印提示信息和电影宣传画
        print('正在为您预订电影《{}》的座位...'.format(name))
        print(symbol)

        # 打印预订座位的方法列表
        print('支持的座位预订方式如下：')
        print("1 - 指定行列号预定座位")
        print("2 - 给我预订一个最靠前的座位！")

        # 获取座位预订方式
        method = input('请选择座位预订方式')
        # valid_method = [str(i + 1) for i in range(2)]
        valid_method = ['1', '2']
        while method not in valid_method:
            method = input('没有按照要求输入哦，请重新输入')
        booking = SeatBooking()
        booking.check_bookings(seats_list)
        if method == '1':
            booking.book_seat(seats_list)
        else:
            booking.book_seat_at_front(seats_list)

    # 打印欢迎语
    def welcome(self):
        print('+      欢迎来到时光电影院       +')

    # 打印结束语
    def bye(self):
        print('+    已经退出系统，下次见！👋    +')


# 实例化 Controller 类
s = Controller(infos)
