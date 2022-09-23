while True:
    s=input('请输入姓名，输入Q时结束:')
    if s=='Q':
        break    # 退出True
    for c in s:
        if c=='E':
            break  # 退出for
        print(c,end='')
    print('\n')
print('程序退出')
