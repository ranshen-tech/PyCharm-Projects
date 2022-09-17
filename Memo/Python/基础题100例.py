# 2.数字阶乘
"""
6的阶乘：6*5*4*3*2*1
3的阶乘：3*2*1
"""

# def factorial(number):
#     result = 1
#     origin = number
#     while number > 0:
#         result *= number
#         number -= 1
#     print(f'{origin}的阶乘是{result}')
#
#
# factorial(3)
# factorial(6)
# factorial(10)


# 3.求圆的面积
# import math
#
#
# def area_of_circle(r):
#     return f'半径为{r}的圆的面积是：{round(math.pi * r ** 2, 2)}'
#
#
# print(area_of_circle(2))
# print(area_of_circle(3.14))
# print(area_of_circle(6.78))


# 4.区间内的所有素数（质数）
"""
输入开始数字和结束数字[begin，end]
打印区间内的所有素数（大于1的整数中，只能被1和自己整除）
"""

# def is_prime(number):
#     if number == 2:
#         return True
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
#
# def print_prime(x, y):
#     for i in range(x, y + 1):
#         if is_prime(i):
#             print(f'{i} is a prime!')
#
#
# begin = 11
# end = 25
# print_prime(begin, end)


# 5.求前n个数字的平方和
"""
输入：正整数N
计算：1^2 + 2^2 + 3^2 + ......+ N^2
"""

# def sum_of_square(n):
#     result = 0
#     for i in range(n + 1):
#         result += i ** 2
#     return f'Sum of square {n} is {result}'
#
#
# print(sum_of_square(3))
# print(sum_of_square(5))
# print(sum_of_square(10))


# 6.计算列表数字的和
# def sum_of_list(lst):
#     total = 0
#     for i in lst:
#         total += i
#     return f'Sum of list {lst} is {total}'
#
#
# lst1 = [1, 2, 3, 4]
# lst2 = [17, 5, 3, 5]
# print(sum_of_list(lst1))
# print(sum_of_list(lst2))
# print(sum(lst1))
# print(sum(lst2))


# 7.计算数字范围内[x, y}的所有偶数
# begin = 4
# end = 15
# data = [i for i in range(begin, end) if i % 2 == 0]
# print(f'begin = {begin}, end = {end}, even number is {data}')


# 8.移除列表中的多个元素
"""
输入：[3, 5, 7, 9, 11, 13]
移除元素：[7, 11]
"""

# lst1 = [3, 5, 7, 9, 11, 13]
# lst2 = [7, 11]
# data = [i for i in lst1 if i not in lst2]
# print(f'From {lst1} remove {lst2}, result: {data}')


# 9.对列表进行元素去重
# lst = [10, 20, 30, 10, 20]
# print(f'Source list is {lst}, unique list is {list(set(lst))}')


# 11.实现学生成绩排序
"""
复杂列表：元素是字典或元组
"""
# stu = [
#     {'id': 1001, 'name': 'rs', 'grade': 88},
#     {'id': 1002, 'name': 'zyc', 'grade': 77},
#     {'id': 1003, 'name': 'cyy', 'grade': 99},
#     {'id': 1004, 'name': 'xp', 'grade': 66}
# ]
#
# sort_stu = sorted(stu, key=lambda x: x['id'], reverse=True)  # x表示列表中的每一个元素
# print(f'Source: {stu},\nsort result: {sort_stu}')


# TODO 12.读取成绩文件排序数据
"""
输入
"""


# 13.统计学生成绩高分、低分、平均分


# 14.
