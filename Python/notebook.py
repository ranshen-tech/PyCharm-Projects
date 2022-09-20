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


# TODO 记得把safari浏览器怎么收藏网页搞明白
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
