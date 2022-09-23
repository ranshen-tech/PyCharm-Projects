# 计算n的阶乘
def fact(n):
    s=1 # 存储乘积
    for i in range(1,n+1):
        s*=i  # 相当于s=s*i
    return s

# 函数的调用
res=fact(4) # 4的阶段
print(res)

print(fact(5))
print(fact(6))
print(fact(7))
