"""
数据定义的类
"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date  # 订单日期
        self.order_id = order_id  # 订单id
        self.money = money  # 订单金额
        self.province = province  # 销售省份
