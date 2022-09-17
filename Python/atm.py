"""
全局变量：money，记录银行卡余额(默认5_000_000)
全局变量：name，用录客户姓名(启动程序时用)
定义如下的函数:
1. 查询余额函数
2. 存款函数
3. 取款函数
4. 主菜单函数

要求：
- 程序启动后要求输入客户姓名
- 查询1.2.3.后返回4.
- 2.3.后应显示1.
- 客户选择退出或输入错误程序才会break
"""
money = 5_000_000
name = input('请输入您的姓名：')


# 定义查询函数
def query(show_header):
    if show_header:
        print('-' * 10, '查询余额', '-' * 10)
    print(f'{name}, 您的余额：{money}元')


# 定义存款函数
def saving(n):
    global money  # money在函数内部定义为全局变量
    money += n
    print('-' * 10, '存款', '-' * 10)
    print(f'{name}👋，您存款{n}元成功')
    # 查询
    query(0)


# 定义取款函数
def get_money(n):
    global money  # money在函数内部定义为全局变量
    money -= n
    print('-' * 10, '取款', '-' * 10)
    print(f'{name}👋，您取款{n}元成功')
    # 查询
    query(0)


# 定义主菜单函数
def main():
    print('-' * 10, '主菜单', '-' * 10)
    print(f'{name}👋，欢迎来到🦄️🏧，请选择操作：')
    print(f'查询余额\t[输入1]')
    print(f'存款\t\t[输入2]')  # 通过\t制表符对齐输出
    print(f'取款\t\t[输入3]')
    print(f'退出\t\t[输入4]')
    return input(f'请输入选择: ')


while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query(1)
        continue  # 每次查询、存款、取款后都返回主菜单
    elif keyboard_input == '2':
        num = int(input('您想要存多少钱? '))
        saving(num)
        continue
    elif keyboard_input == '3':
        num = int(input('您想要取多少钱？'))
        get_money(num)
        continue
    else:
        print('程序退出')
        break

