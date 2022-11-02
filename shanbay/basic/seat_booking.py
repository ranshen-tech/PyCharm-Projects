__author__ = 'ranshen0519@icloud.com'

import time


class SeatBooking:
    def get_row(self):
        input_row = int(input("预订第几排的座位呢？请输入 1～6 之间的数字"))
        valid_row = [i + 1 for i in range(6)]
        while input_row not in valid_row:
            input_row = int(input('没有按要求输入哦，请输入 1～6 之间的数字'))
        row = input_row - 1
        return row

    def get_col(self):
        input_column = int(input('预订这一排的第几座呢？请输入 1～8 之间的数字'))
        valid_column = [i + 1 for i in range(8)]
        while input_column not in valid_column:
            input_column = int(input('没有按要求输入哦，请输入 1～8 之间的数字'))
        column = input_column - 1
        return column

    # 展示座位预订信息
    def check_bookings(self, seats):
        print("正在为您查询该场次电影的预订状态...")
        time.sleep(0.7)
        print('从上到下为 1～6 排，从左至右为 1～8 座')
        print("======================")
        for row in seats:
            time.sleep(0.1)
            print('\t'.join(row))
        print("======================")
        time.sleep(0.7)

    # 预订座位
    def book_seat(self, seats):
        while True:
            row = self.get_row()
            column = self.get_col()
            if seats[row][column] == '○':
                print("正在为您预订指定座位...")
                time.sleep(0.7)
                seats[row][column] = '●'  # 预订成功，该座位将被标记为“已预约”
                print(f"预订成功！座位号：{row+1}排{column+1}座")
                break
            else:
                print("这个座位已经被预订了哦, 试试别的吧")
                time.sleep(0.7)
