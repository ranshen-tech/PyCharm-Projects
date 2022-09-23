def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=eval(input('请输入数字:'))
print(fib(n))

