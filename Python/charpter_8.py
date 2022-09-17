import time

# f = open('test.txt', 'r', encoding='UTF-8')
# fw = open('test.txt', 'w', encoding='UTF-8')
# fa = open('test.txt', 'a', encoding='UTF-8')
# print(type(f))
# print(type(fw))
# print(type(fa))

# print(type(f))
# f.read(num) num表示从文件中读取的数据的长度,没有num默认读取所有数据
# print(type(f.read()))
# print(f'read方法读取10个字节的结果: {f.read(10)}')
# print(f'read方法读取全部内容的结果: {f.read()}')  # 多次调用read()方法会在之前读取的内容后继续读取


# f.readlines() 按照行的方式把整个文件内容一次性读取，返回的是列表，每一行是一个元素
# lines = f.readlines()
# print(type(lines))
# print(f'readlines方法读取全部内容的结果: {lines}')


# f.readline() 一次读取一行内容
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f'第1行数据是：{line1}')
# print(f'第2行数据是：{line2}')
# print(f'第3行数据是：{line3}')


# for循环♻️读取文件对象
# for line in f:
#     print(f'每一行数据是：{line}')


# 文件的关闭
# time.sleep(5)
# f.close()


# with open语法
# with open('test.txt', 'r', encoding='UTF-8') as f:
#     for line in f:  # 一次循环得到一行数据
#         print(f'每一行的数据是: {line}')


# 写操作'w'(打开不存在文件）
# f = open('sunnyday.txt', 'w', encoding='UTF-8')
# f.write('ranshen')

# f.flush()  # 内容刷新
# f.close()  # 包含flush()功能
# time.sleep(6000)


# 写操作'a'
# f = open('heima.txt', 'a', encoding='UTF-8')
# f.write('\n月薪过万')
# f.flush()
# f.close()


#
