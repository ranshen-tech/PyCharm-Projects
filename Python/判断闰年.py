# 闰年：能被4整除，不能被100整除；或者能被400整除
while True:
    year = int(input(': '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('yes')
        break
    else:
        print('no')
