__author__ = 'ranshen0519@icloud.com'


def get_row():
    input_row = int(input("预订第几排的座位呢？请输入 1～6 之间的数字"))
    valid_row = [i for i in range(1, 7)]
    while input_row not in valid_row:
        input_row = int(input('没有按要求输入哦，请输入 1～6 之间的数字'))
    row = input_row - 1
    return row


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

    @staticmethod
    def book_seat_at_front(seats):
        print("正在为您预订最靠前的座位...")
        for row in range(6):
            for column in range(8):
                if seats[row][column] == '○':
                    seats[row][column] = '●'  # 预订该座位
                    print("预订成功！座位号：{}排{}座".format(row + 1, column + 1))
                    return  # 结束函数的执行，返回到它被调用的地方
        print("非常抱歉🥺，所有座位都被订满了，无法为您保留座位")
