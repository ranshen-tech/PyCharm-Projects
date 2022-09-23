# 闰年
while True:
    try:
        year=eval(input('请输入一个年份:'))
        if (year%4==0 and year%100!=0) or year%400==0:
            print(year,'是闰年')
        else:
            print(year,'不是闰年')
        break
    except:
        print('输入内容必须为整数！请重新输入')
        continue

    
    
