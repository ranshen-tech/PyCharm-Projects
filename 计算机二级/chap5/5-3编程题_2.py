from math import sqrt

def isPrime(n):
    if n==1:
        return False
    
    #对于正整数n,如果用2到根据n之间的所有整数去除，均无法整除，则n为质数
    
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

try:
    n=eval(input('请输入要判断的数字:'))
    print(isPrime(n))
except:
    print('格式输入错误，一定要整数正整数')

    
