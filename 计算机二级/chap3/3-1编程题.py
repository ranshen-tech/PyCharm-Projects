num=eval(input('请输入一个整数:'))
if 0<=num<=99:
    print('请输入一个三位数的整数')
else:
    num//=100
    print('百位及以上的数字为:{0}'.format(num))
