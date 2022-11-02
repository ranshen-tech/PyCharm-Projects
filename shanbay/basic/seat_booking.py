class SeatBooking:
    @staticmethod
    def get_row():
        input_row = int(input("预订第几排的座位呢？请输入 1～6 之间的数字"))
        valid_row = [i for i in range(1, 7)]
        while input_row not in valid_row:
            input_row = int(input('没有按要求输入哦，请输入 1～6 之间的数字'))
        row = input_row - 1
        return row

    @staticmethod
    def get_col():
        input_column = int(input('预订这一排的第几座呢？请输入 1～8 之间的数字'))
        valid_column = [i for i in range(1, 9)]
        while input_column not in valid_column:
            input_column = int(input('没有按要求输入哦，请输入 1～8 之间的数字'))
        column = input_column - 1
        return column

    @staticmethod
    def check_bookings(seats):
        print("正在为您查询该场次电影的预订状态...")
        for row in seats:
            time.sleep(0.1)
            print('\t'.join(row))
        print("======================")

    def book_seat(self, seats):
        while True:
            row = self.get_row()
            column = self.get_col()
            if seats[row][column] == '○':
                print("正在为您预订指定座位...")
                seats[row][column] = '●'
                print(f"预订成功！座位号：{row + 1}排{column + 1}座")
                break
            else:
                print("这个座位已经被预订了哦, 试试别的吧")
