"""
2022-09-18
"""
# 字符串驻留机制：拼接🪢和修改字符串影响性能；用join代替拼接'+'
# ord() chr() 请你猜猜我的名字
# s = 'ranshen'
# print(s.count('n', 1))

# 字符串编码/解码
# s = '冉申'
# es = s.encode(encoding='utf-8')
# print(es)
# print(type(es))
# ds = es.decode(encoding='utf-8')
# print(ds)
# print(type(ds))

# 字符串格式化
# name = '冉申'
# age = 18
# print('姓名%s, 年龄%d' % (name, age))
# print('姓名{}, 年龄{}'.format(name, age))
# print(format())


# 身份证号自动识别出身日期（提供N个身份证号，提取年月日）


# 取余运算
# 17(被除数) / (-3)(除数) = -6(商)······-1(余数)
# 被除数 = 除数 * 商 + 余数
# 商 = (被除数 - 余数) / 除数
# 余数是除法的商向小取整，余数符号同除数
# print(17 % -3)  # 商-6 余-1
# print(-17 % 3)  # 商-6 余1
# print(-17 % -3)  # 商 -5 余-2


"""
2022-09-19
"""
# 输入一个十进制整数，分别输入二进制，八进制，十六进制字符串
# num = int(input('请输入一个十进制整数：'))
# print(f'{num}的二进制数为：{bin(num)}')
# print(f'{num}的八进制数为：{oct(num)}')
# print(f'{num}的十六进制数为：{hex(num)}')


# 最大公约数：如存在x满足a，b均可以整除x，则x为a，b的公约数，当x最大时为最大公约数
# a = int(input('请输入整数a：'))
# b = int(input('请输入整数b ：'))
# x = 0
# assert a > 0 and b > 0, '请输入正整数!'
# min_num = min(a, b)
# max_num = max(a, b)
# for x in range(min_num, 0, -1):  # 倒着遍历
#     if a % x == 0 and b % x == 0:
#         break
# print(f'{a}和{b}的最大公约数是：{x}')
# 最小公倍数：如存在y满足a，b均可以被整除，则y为a，b的公倍数，当y最小时为最小x公倍数
# while True:
#     if max_num % a == 0 and max_num % b == 0:
#         break
#     max_num += 1
# print(f'{a}和{b}的最小公倍数是：{max_num}')


# 统计不同字符个数
# string = input('请输入一行字符串：')
# alpha, num, space, other = 0, 0, 0, 0
# for i in string:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         num += 1
#     elif i.isspace():
#         space += 1
#     else:
#         other += 1
# print(f'字母字符{alpha}, 数字字符{num}, 空格字符{space}, 其他字符{other}')


# 求阶乘函数
# def factorial(n):
#     total = 1
#     for i in range(n, 0, -1):
#         total *= i
#     return total


# print(factorial(5))


"""
2022-09-20
"""

# json本质上是特定格式的字符串：数据格式是字典，或者内部嵌套字典的列表
# 演示json数据和python字典相互转换
# import json

# 准备列表，列表中每一个元素都是字典，将其转换为json
# data = [{'name': 'rs', 'age': 29}, {'name': 'zyc', 'age': 38}, {'name': 'cyy', 'age': 16}]
# 通过json.dumps(data)方法把python数据转化为json数据
# json_str = json.dumps(data)
# print(type(json_str))
# print(json_str)


# 准备字典，将字典转换为json
# d = {'name': '周杰伦', 'addr': '台北'}
# json_str = json.dumps(d, ensure_ascii=False)
# print(type(json_str))
# print(json_str)


# 通过json.loads(data)方法把json字符串转化为python数据
# string = '[{"name": "rs", "age": 29}, {"name": "zyc", "age": 38}, {"name": "cyy", "age": 16}]'
# lst = json.loads(string)
# print(type(lst))
# print(lst)

# string = '{"name": "周杰伦", "addr": "台北"}'
# lst = json.loads(string)
# print(type(lst))
# print(lst)


# pycharts基础入门
# 导包，导入line功能构建折线图对象
# from pyecharts.charts import Line
# 导包，导入各种控制选项
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 通过line函数得到折线图对象
# line = Line()
# 添加x轴数据
# line.add_xaxis(['中国', '美国', '英国'])
# 添加y轴数据
# line.add_yaxis('GDP', [30, 20, 10])

# 全局配置通过set_global_opts()方法
# line.set_global_opts(
#     title_opts=TitleOpts(title='Gdp展示', pos_left='center', pos_bottom='1%'),  # 光标移到括号里按command + p可以把需要的参数都弹出来
#     legend_opts=LegendOpts(is_show=True),  # 图例
#     toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱
#     visualmap_opts=VisualMapOpts(is_show=True)  # 视觉映射
# )

# 生成图像
# line.render()


# 全局变量在函数内部使用时需要提前使用global声明
# n = 2
# def multiply(x, y=10):
#     return x * y * n  # 未使用global，即使n名称相同，也不是全局变量


# s = multiply(3, 4)
# print(s)


# def multiply(x, y=10):
#     global n
#     n = x * y
#     return n


# s = multiply(99, 2)
# print(s)
# print(n)


# string = "an apple a day"
# def split(s):
#     return s.split('a')
# print(split(string))


# def func(ls=[]):
#     ls.append(1)
#     return ls
# a = func()
# b = func()
# print(a, b)


# 判断质数
# def isPrime(n):
#     if n <= 1:
#         return False
# 对于正整数n，如果用2-n之间的所有整数去除，均无法整除，那么n是质数（只能被1和自己整除）
# for i in range(2, n):
#     if n % i == 0:
#         return False
# else:
#     return True
# try:
#     num = eval(input('请输入要输入的数字：'))
#     print(isPrime(num))
# except Exception as e:
#     print(f'发现异常：{e}')
#     print('一定要整数，正整数')

# for j in range(201):
#     if isPrime(j):
#         print(j, end=' ')


# 组合数据类型：集合、序列、映射
# 集合操作符：
# S-T(差集)在S中但不在T中;S&T(交集)同时在S和T中；S^T(补集)S和T中非共同元素;S|T(并集)S和T中所有元素
# s = {1, 2, 3}
# t = {3, 4, 5}
# print(s - t)
# print(s & t)
# print(s ^ t)
# print(s | t)


"""
2022-09-21
"""
# sort()参数key是某个函数的返回值，这个函数的输入参数是我们要待排序的列表的每一个元素，
# 返回值作为我们对列表元素进行排序的依据
# lst = [[1, 7], [1, 5], [2, 4], [1, 1]]
# lst.sort()
# print(lst)
# lst.sort(key=lambda x: x[1])
# print(lst)


# 随机密码生成：26个字母和9位数组成的列表中随机生成10个8位密码
# import random
# lst1 = [chr(i) for i in range(97, 123)]  # 26个字母的列表
# lst2 = [i for i in range(10)]  # 10个数字的列表
# result = lst1 + lst2
# for i in range(10):
#     for j in range(8):
#         print(random.choice(result), end='')
#     print()


# 逗号分隔的储存格式脚CSV，采用join方法最方便
# a = '1234'
# b = 'a'.join(a)
# print(b)


# 最好用列表推导式


# case = [9, 8, 8, 3, 3, 1]
# for i in case:
#     if i % 2 == 0:
#         case.remove(i)
# print(case)  # 为啥结果不是[9, 3, 3, 1]
# case1 = [i for i in case if i % 2 == 0]
# print(case1)
# case2 = [i for i in case if i % 2 != 0]
# print(case2)


"""
2022-09-23
"""
# 查看python版本
# import sys
# print(sys.version)


"""
2022-09-24
"""


# 设计一个类
# class Student:
#     name = None

# def say_hi(self):  # 方法中访问成员变量必须用self
#     print(f'hi, i am {self.name}，请多多关照')

# def say_hi2(self, msg):
#     print(f'大家好，我是{self.name}, {msg}')  # msg不是成员变量，是外部传入的，不用加self


# 创建一个对象
# stu = Student()
# 对象属性赋值
# stu.name = '林俊杰'
# stu.age = 31
# 获取对象中的信息
# print(stu.age)
# print(stu.name)
# stu.say_hi2('小伙子我看好你')

# stu2 = Student()
# stu2.name = '周杰伦'
# stu2.say_hi2('哎哟不错哟')


# 创建⏰类
# class Clock:
#     id = None  # 序列
#     price = None  # 价格
# def ring(self):
#     import os
#     os.system("say 'hi'")

# 构建对象
# clock1 = Clock()
# clock1.id = '001'
# clock1.price = 19.99
# print(f'⏰id：{clock1.id}, 价格：{clock1.price}')
# clock1.ring()


# class Student:
#     name = None
#     age = None
#     tel = None
# def __init__(self, name, age, tel):
#     self.name = name
#     self.age = age
#     self.tel = tel
#     print('Student类创建了一个类对象')
# stu = Student('周杰伦', 31, '1850000666')
# print(stu.name)
# print(stu.age)
# print(stu.tel)


# 练习
# class Student:
#     def __init__(self, name, age, addr):  # 构造方法
#         self.name = name
#         self.age = age
#         self.addr = addr
#         print(f'学生{i}信息录入完成✅，信息为：【学生姓名：{self.name}年龄：{self.age}地址:{self.addr}】')
# for i in range(1, 4):
#     print(f'当前录入第{i}位学生信息')
#     n = input('请输入学生姓名：')
#     a = input('请输入学生年龄：')
#     ad = input('请输入学生地址：')
#     stu = Student(n, a, ad)


# 魔术方法
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# __str__魔术方法
# def __str__(self):
#     return f'Student类对象，name：{self.name}, age：{self.age}'
# __lt__魔术方法(less than)
# def __lt__(self, other):
#     return self.age < other.age
# __le__魔术方法(less than or equal to)
# def __le__(self, other):
#     return self.age <= other.age
# __eq__魔术方法(equal) 返回True or False
# def __eq__(self, other):
#     return self.age == other.age
# stu1 = Student('周杰伦', 31)
# stu2 = Student('林俊杰', 31)
# print(stu1)
# print(stu1 < stu2)
# print(stu1 <= stu2)
# print(stu1 == stu2)


# 面向对象封装📦思想中私有成员的使用(只可以内部自己使用)
# class Phone:
#     __current_voltage = 0.5  # 当前运行电压

    # def __keep_single_core(self):
    #     print('让cpu以单核模式运行')

    # def call_by_5g(self):
    #     if self.__current_voltage >= 1:
    #         print('5g通话已开启')
    #     else:
    #         self.__keep_single_core()
    #         print('电量不足，无法使用5g通话，以设置单核运行进行省电。')
# phone = Phone()
# phone.call_by_5g()


# 练习：设计一个带有私有成员的手机
# class Phone:
#     __is_5g_enable = False

    # def __check_5g(self):
    #     if self.__is_5g_enable:
    #         print('5g开启')
    #     else:
    #         print('5g关闭，使用4g网络')

    # def call_by_5g(self):
    #     self.__check_5g()
    #     print('正在通话中')

# phone = Phone()
# phone.call_by_5g()
