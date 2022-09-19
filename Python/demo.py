# a, b,  *d = 'room'
# print(a, b, d)


# tuple1 = (i for i in range(10) if i % 2 == 0)
# print(tuple1)
# print(tuple(tuple1))


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


# for i in 'python':
#     for j in range(2):
#         print(i, end='')
#         if i == 'h':
#             break


# import random


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


# 2022918
# lst1 = [1, 2, 3, 4, 5]
# lst2 = ['python', 'java', 'javascript', 'rust']
# z = zip(lst1, lst2)
# x = tuple(z)
# print(dict(tuple(zip(lst1, lst2))))

# a = (('apple', 'a'), ('b', 'banana'), ('c', 'cat'))
# b = list(a)
# print(b)
# print(dict(b))


# t = (i for i in range(10) if i % 2)
# print(tuple(t))

# d = {i: i + 2 for i in range(10) if i % 2}
# print(d)


# 集合是可变数据类型，集合中的元素必须是不可变数据类型,集合没有索引，但集合中元素可以for遍历
# lst = (1, 2, 3)
# s = set(lst)
# print(s)
# s.add(22)
# print(s)
# for i in s:
#     print(i)

# s = {'apple', 'banana', 'grape', 'pear', 'orange'}
# d = {'apple': 1, 'banana': 2, 'grape': 3, 'pear': 4, 'orange': 5}
# print(s)
# print(d)
