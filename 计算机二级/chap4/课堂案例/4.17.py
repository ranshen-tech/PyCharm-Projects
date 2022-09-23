try:
    a=eval(input('请输入被除数:'))
    b=eval(input('请输入除数'))
    print(a/b)
except  ZeroDivisionError:
    print('0不可以为除数')
except:
    print('其它的异常')
