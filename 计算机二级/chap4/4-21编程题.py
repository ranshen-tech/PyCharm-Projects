s=input("请输入一行字符：\n")
alpha,num,space,other=0,0,0,0
for i in s:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        num+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print('英文字符数:{},数字字符数:{}'.format(alpha,num))
print('空格字符数:{},其它字符数:{}'.format(space,other))


