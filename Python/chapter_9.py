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


# [from 模块名] import [模块｜类｜变量｜函数｜*] [as 别名]
# 使用import导入time模块使用sleep功能（函数）
# import time  # 导入内置time模块(time.py这个代码文件)
# command + f搜索文档中的sleep()函数
# print('hi')
# time.sleep(3)  # 通过.就可以使用模块内部所有功能（类、函数、变量）
# print('hello')


# 使用form导入time模块使用sleep功能（函数）
# from time import sleep
# print('hi')
# sleep(3)
# print('haha')


# 使用*导入time模块全部功能（函数）
# from time import *
# print(1)
# sleep(3)
# print(4)


# 使用as给特定功能加上别名
# import time as t
# print(1)
# t.sleep(3)
# print(4)

# from time import sleep as sl
# print(1)
# sl(3)
# print(4)


# 自定义模块的引用
# import my_module_1
# from my_module_1 import test
# test(1, 2)

# TODO 直接赋值，粘贴（稍微修改）文件就能创建新文件


# 导入不同模块的同名功能
# from my_module_2 import test
# test(1, 2)


# __main__变量：只有当程序直接执行才会进入if内部，如果是被导入的，则if无法进入


# __all__变量：模块文件中有__all__变量，当使用`from xxx import *`导入时，只能导入这个列表中的元素
# from my_module_1 import *
# test_a(1, 2)
# test_b(2, 1)


# 导入包(方式1）：
# import 包名.模块名
# 包名.模块名.目标
# import my_package.my_module_1
# import my_package.my_module_2®
# my_package.my_module_1.info_print_1()
# my_package.my_module_2.info_print_2()


# from my_package import my_module_1
# from my_package import my_module_2
# my_module_1.info_print_1()
# my_module_2.info_print_2()


# from my_package.my_module_1 import info_print_1
# from my_package.my_module_2 import info_print_2
# info_print_1()
# info_print_2()


# 导入包（方式2）：
# from 包名 import *  必须在`__init__.py`文件添加`__all__ = []`,控制允许导入的模块列表
# 模块名.目标
# from my_package import *
# my_module_1.info_print_1()
# my_module_2.info_print_2()



