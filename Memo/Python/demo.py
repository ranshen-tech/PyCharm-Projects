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
