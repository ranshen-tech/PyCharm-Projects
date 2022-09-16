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


