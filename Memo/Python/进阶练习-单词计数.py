"""读取word.txt文件
统计'itheima'单词出现次数
"""
# 方法一
# with open('word.txt', 'r', encoding='UTF-8') as f:
#     count = 0
#     for line in f:
#         for word in line.split():
#             if word == 'itheima':
#                 count += 1
# print(f'"itheima"出现了{count}次')


# 方法二
with open('word.txt', 'r', encoding='UTF-8') as f:
    print(f.read().count('itheima'))


