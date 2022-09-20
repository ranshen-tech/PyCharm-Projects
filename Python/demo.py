# a, b,  *d = 'room'
# print(a, b, d)


# 使用参数创建字典
# d = dict(cat=10, dog=20)  # 参数相当于变量，变量的名字不加引号
# print(d)


# 可以直接使用dict函数将[(1, 'rs'), (2, 'cyy'), (3, 'xp')]转成字典
# lst = [(1, 'rs'), (2, 'zyc'), (3, 'xp')]
# d = dict(lst)
# print(d)


# 字典生成
# import random
# d = {key: random.randint(1, 3) for key in range(5)}
# print(d)


# 使用映射函数生成字典
# name = ['rs', 'zyc', 'cyy']
# age = [29, 18, 21]
# d = {key: value for key, value in zip(name, age)}
# print(d)


# lst1 = [1, 2, 3, 4, 5]
# lst2 = ['python', 'java', 'javascript', 'rust']
# z = zip(lst1, lst2)
# print(z)
# x = tuple(z)
# print(x)
# print(dict(tuple(zip(lst1, lst2))))


# a = (('apple', 'a'), ('b', 'banana'), ('c', 'cat'))
# b = list(a)
# print(b)
# print(dict(b))
# print(dict(a))


# d = {i: i + 2 for i in range(10) if i % 2}
# print(d)


# 集合是可变数据类型，集合中的元素必须是不可变数据类型,集合没有索引，但集合中元素可以for遍历
