for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()


i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的控制语句，通过\t制表符对齐，不换行
        print(f'{j} * {i} = {j * i}', end='\t')
        j += 1

    print()  # 空内容，就是输出一个换行
    i += 1
print('😍')
