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
# try:
    # 1 / 1
    # print('name')
    # open('sdfsf.txt', 'r')
# except Exception as e:
#     print('出现异常了！')
#     print(e)
# else:  # 如果没有出现异常则执行
#     print('没有出现异常')
# finally:  # 无论是否异常都要执行的

f = 0
try:
    print('start...')
    f = open('a.txt', 'r')
    print(f)
    print('try...')
except Exception as e:
    print(f'发现异常: {e}')
    f = open('a.txt', 'w')
else:
    print('没有出现异常')
finally:
    print('有没有异常我都要执行')
    f.close()
