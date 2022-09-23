def num(s):
    a=b=c=d=0
    for i in s:
        if i.isdigit():
            a+=1
        elif i.isalpha():
            b+=1
        elif i.isspace():
            c+=1
        else:
            d+=1
    print('数字{}个,字母{}个，空格{}个，其他字符{}个'.format(a,b,c,d))

s=input('请输入一个字符串:')
num(s)

