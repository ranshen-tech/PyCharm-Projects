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
        print(f'right, 你猜了{i}次')
        break
    else:
        if guess_num > num:
            print('more')
        else:
            print('little')

```
