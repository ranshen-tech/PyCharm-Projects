# a, b,  *d = 'room'
# print(a, b, d)


# a, *b = 'room'
# print(a, b)


# list1 = [i for i in range(10) if i % 2 == 0]
# print(list1)
#
# tuple1 = (i for i in range(10) if i % 2 == 0)
# print(tuple1)
# print(list(tuple1))
#
# set1 = {i for i in range(10) if i % 2 == 0}
# print(set1)
#
# dict1 = {i for i in range(10) if i % 2 == 0}


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} * {i} = {j * i}', end='\t')
#     print()


# for i in range(5):
#     for j in range(i + 1):
#         print('*', end='\t')
#     print()
# print('\n')
#
#
# for i in range(5):
#     for j in range(5 - i):
#         print('*', end='\t')
#     print()
# print('\n')

#
# top = int(input('请输入菱形上半部分有多少行：'))
# bot = top - 1
#
# for i in range(top):
#     for j in range(bot - i):
#         print(' ', end='')
#     print('*' * (1 + 2 * i))
#
# for i in range(bot):
#     for j in range(i + 1):
#         print(' ', end='')
#     print('*' * (2 * (bot - i) - 1))

#
# for i in 'python':
#     for j in range(2):
#         print(i, end='')
#         if i == 'h':
#             break


# import random
#
#
# lst = [random.random() for _ in range(10)]
# print(lst)


# lst = [[j for j in range(3)] for i in range(4)]
# print(lst)

#
# # zip函数的使用  函数映射的结果是zip对象
# lst1 = [1, 2, 3, 4]
# lst2 = ['rs', 'zyc', 'cyy', 'xp']
# zip1 = zip(lst1, lst2)
# zip2 = zip(lst2, lst1)
# print(zip1)
# print(zip2)
# print(list(zip1))
# print(list(zip2))
# d = dict(zip1)
# print(d)
# print(dict(zip2))


# # 使用参数创建字典
# d = dict(cat=10, dog=20)  # 参数相当于变量，变量的名字不加引号
# print(d)


# t = (1, 2, 3)
# d = {t: 10}
# print(d)


# 可以直接使用dict函数将[(1, 'rs'), (2, 'cyy'), (3, 'xp')]转成字典
# lst = [(1, 'rs'), (2, 'zyc'), (3, 'xp')]
# d = dict(lst)
# print(d)


# # pop方法
# print(d.pop(1))
# print(d)
# print(d.pop(111, '不存在'))
# print(d)


# 字典生成
# import random
#
#
# d = {key: random.randint(1, 3) for key in range(5)}
# print(d)


# # 使用映射函数生成字典
# name = ['rs', 'zyc', 'cyy']
# age = [29, 18, 21]
# d = {key: value for key, value in zip(name, age)}
# print(d)


# # 集合生成式
# s = {i for i in range(10) if i % 2}
# print(s)


# 练习
# d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# d2 = d
# d['b'] = 100
# print(d['b'] + d2['b'])


# lst = []
# for i in '想念':
#     for j in '家人':
#         lst.append(i + j)
# print(lst)


# lst = [1, 3, 5, 7, 9]
# print(lst.reverse())
