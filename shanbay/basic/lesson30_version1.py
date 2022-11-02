__author__ = 'ranshen0519@icloud.com'
import time


class SeatBooking:
    # 查询预订状态
    def check_bookings(self, seats: list):
        print("正在为您查询该场次电影的预订状态...")
        time.sleep(0.7)
        print('从上到下为 1～6 排，从左至右为 1～8 座')
        # 为了让输出结果更美观，额外打印两行分隔线
        print("======================")
        # 逐行打印座位表中的预订信息
        for row in seats:
            time.sleep(0.1)
            print('\t'.join(row))
        print("======================")
        time.sleep(0.7)

    # 指定座位号预订座位
    def book_seat(self, seats: list):
        # 获取用户输入，转换为二维列表的行索引和列索引
        row = int(input("预订第几排的座位呢？请输入 1～6 之间的数字")) - 1
        column = int(input("预订这一排的第几座呢？请输入 1～8 之间的数字")) - 1
        # 如果列表中对应值为 '○' 则预订成功，否则预订失败
        if seats[row][column] == '○':
            print("正在为您预订指定座位...")
            time.sleep(0.7)
            seats[row][column] = '●'  # 预订成功，该座位将被标记为“已预约”
            print(f"预订成功！座位号：{row+1}排{column+1}座")
        else:
            print("这个座位已经被预订了哦")


seats_list = [['○', '○', '○', '○', '○', '○', '○', '○'],
              ['○', '○', '○', '○', '●', '○', '○', '●'],
              ['○', '○', '●', '○', '●', '○', '○', '○'],
              ['○', '○', '●', '○', '○', '○', '○', '●'],
              ['○', '○', '●', '○', '○', '○', '●', '○'],
              ['●', '○', '○', '○', '●', '●', '●', '●']]

# 实例化 SeatBooking 类
booking = SeatBooking()
# 调用 SeatBooking 类的 check_bookings() 方法
booking.check_bookings(seats_list)
# 按用户输入的座位号预订座位
booking.book_seat(seats_list)
