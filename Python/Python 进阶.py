# 2022/9/14 10:03

# # 支持不同类型的数据return
# def test_return():
#     return 1, 'hello', True
#
#
# x, y, z = test_return()
# print(x)
# print(y)
# print(z)


# def user_info(name, age, gender='female'):
#     print(f'姓名是：{name}，年龄是：{age}， 性别是：{gender}')
#
#
# user_info('ranshen', 33, 'male')


# 位置传递
# def user_info(*args):
#     print(f'user_info参数的类型是：{type(args)}, 内容是：{args}')
#
#
# user_info('ran')
# user_info('ran', 18)


# # 关键字传递
# # 参数是'键=值'形式的情况下，所有'键=值'都会被kwargs接受，同时会根据'键=值'组成字典
# def user_info(**kwargs):
#     print(f'user_info参数的类型是：{type(kwargs)}, 内容是：{kwargs}')
#
#
# user_info(name='ran', age=18, id=110)
# user_info(gender='male')


# 函数作为参数传递
# def test_func(compute):
#     result = compute(1, 2)
#     print(type(compute))
#     print(result)
#
#
# test_func(lambda x, y: x + y)


# 打
