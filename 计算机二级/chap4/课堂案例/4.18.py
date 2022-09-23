import random
target=random.randint(1,1000)
count=0 # 猜的次数
while True:
    guess=eval(input('请输入你猜的数1-1000:'))
    count+=1  #次数加1
    if guess>target:
        print('猜大了')
    elif guess<target:
        print('猜小了')
    else:
        print('猜对了')
        break
print('共猜了',count,'次')
