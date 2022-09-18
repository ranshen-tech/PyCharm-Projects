# 基本捕获语法
# try:
#     f = open('inexistence.txt', 'r', encoding='UTF-8')
# except:
#     print('出现异常了，我将open模式改为w模式试试😍')
#     f = open('inexistence.txt', 'w', encoding='UTF-8')


# 捕获指定异常
# try:
#     print(name)
# 1 / 0
# except NameError as e:
#     print('出现了变量未定义的异常')
#     print(e)


# 捕获多个异常
# try:
# var = 1 / 0
# print(name)
# except (NameError, ZeroDivisionError) as e:
#     print('出现了变量未定义/除以0的异常错误')
#     print(e)


# 捕获所有异常
# f = 0
# try:
#     print('start...')
#     f = open('a.txt', 'r')
#     print(f)
#     print('try...')
# except Exception as e:
#     print(f'发现异常: {e}')
#     f = open('a.txt', 'w')
# else:
#     print('没有出现异常')
# finally:
#     print('有没有异常我都要执行')
#     f.close()


"""
演示异常的传递性
"""


# 定义一个出现异常的方法
# def fun1():
#     print('func1 start')
#     num = 1 / 0  # 肯定有异常，除以0异常
#     print('func1 over')


# 定义一个无异常方法，调用上面方法
# def fun2():
#     print('fun2 start')
#     fun1()
#     print('fun2 over')


# 定义一个方法，调用上面方法
# def main():
#     try:
#         fun2()
#     except Exception as e:
#         print(f'出现异常了，异常的信息是：{e}')


# if __name__ == '__main__':
#     main()


# [from 模块] import [模块｜类｜变量｜函数｜*] [as 别名]
# import time  # 导入内置time模块(time.py这个代码文件)
# command + f搜索文档中的sleep()函数
# print('hi')
# time.sleep(3)  # 通过.就可以使用模块内部所有功能（类、函数、变量）
# print('hello')


# from time import sleep
# print('hi')
# sleep(3)
# print('haha')


