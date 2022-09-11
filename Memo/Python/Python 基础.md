## while循环


### 求1-100的和

```python
sum_ = 0
i = 1
while i <= 100:
    sum_ += i
    i += 1
```


### 判断输入的数字是否等于1-100以内的随机数，并打印猜的次数

```python
import random
num = random.randint(1, 100)

i = 0
while True:
    guess_num = int(input())
    i += 1
    if guess_num == num:
        print('right')
        break
    else:
        if guess_num > num:
            print('more')
        else:
            print('little')
print(f'你猜了{i}次')
```


### 表白100天，每天送10朵🌹

```python
# 外层循环
i = 1
while i <= 10:
    print(f'每天向小美表白，这是第{i}天')
    
    # 内层循环
    j = 1
    while j <= 5:
        print(f'送小美第{j}朵🌹')
        j += 1

    print('小美，我喜欢你')
    i += 1
print(f'坚持到{i - 1}天，表白成功')

```


