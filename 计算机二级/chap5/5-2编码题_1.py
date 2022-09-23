def isNum(a):
   
    if type(a)==int or type(a)==float or type(a)==complex:
       return True
    else:
        return False
a=eval(input('请随机输入一个字符串:'))
print(isNum(a))


