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
# json本质上是特定格式的字符串：数据格式是字典，或者内部嵌套字典的列表都转换为字符串
# 导入json模块
import json

# 准备符合json格式要求的python数据
data = [{'name': 'rs', age = 30}, {'name': 'zyc', age = 18}]
# 通过json.dump(data)方法把python数据转化为json数据
data = json.dump(data)
# 通过json.load(data)方法把json数据转化为python数据
