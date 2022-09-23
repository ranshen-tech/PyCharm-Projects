# 定义一个对整数n求阶乘的函数
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

# 调用整数阶乘的函数
print(fact(5))
print(fact(10))
print(fact(20))


