# 猜数游戏
import random
target=random.randint(1,1000)
count=0
while True:
      guess=eval(input('请输入一个猜测的整数（1至1000）'))
      count+=1
      if guess>target:
            print('猜大了')
      elif guess<target:
            print('猜小了')
      else:
            print('猜对了')
            break
print('此轮的猜测次数是:',count)


