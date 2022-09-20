# 递归就是自己调用自己
def fibo(index):
    if index == 0 or index == 1:
        return 1
    else:
        return fibo(index - 1) + fibo(index - 2)


print(fibo(5))
