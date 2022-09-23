from math import sqrt
def isPrime(n):
    if n==1:
        return False
    
    #对于正整数n,如果用2到根据n之间的所有整数去除，均无法整除，则n为质数
    
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(1,201):
    if isPrime(i):
        print(i,end=' ')
