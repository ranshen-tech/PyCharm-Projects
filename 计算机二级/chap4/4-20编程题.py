# 最大公约数
a=eval(input('请输入一个整数:'))
b=eval(input('请输入另一个整数:'))
x=a*b
while b:
        r = a%b
        a = b
        b = r
    
print('最大公约数为:',a)
# 最小公倍数
print('最小公倍数为:',x//a)



