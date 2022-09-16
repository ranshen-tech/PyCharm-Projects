### 赋值
- **链式赋值**
`a = b = c = 100`
- **交换赋值**
`a, b = b, a`

## while循环


#### 求1-100的和

```python
sum_ = 0
i = 1
while i <= 100:
    sum_ += i
    i += 1
```


#### 判断输入的数字是否等于1-100以内的随机数，并打印猜的次数

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


#### 表白100天，每天送10朵🌹

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


#### 九九乘法表

```python
# 定义外层循环的控制变量
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的控制语句，通过\t制表符对齐，不换行
        print(f'{j} * {i} = {j * i}', end='\t')
        j += 1

    print()  # 空内容，就是输出一个换行
    i += 1
print('😍')
```


## for循环

```python
# 有多少个字母a
string = 'itheima is a brand of itcast'
n = 0
for i in string:
    if i == 'a':
        n += 1
        
print(f'{string}中共含有:{n}个字母a')
```


##### range() 构建一个数字序列

```python
# for循环对变量i进行了覆盖
i = 0
for i in range(5):
    print(i)
    
print(i)

```

```python
# 有几个偶数
num = 100
count = 0
for i in range(1, num):
    if i % 2 == 0:
        count += 1
print(f'有{count}个偶数')
```

```python
# 表白100天，每天都送10朵🌹
i = 0
for i in range(1, 11):
    print(f'今天是向小美表白的第{i}天')
    for j in range(1, 6):
        print(f'送给小美的第{j}朵🌹')
    print('小美，我喜欢你')

print(f'第{i}天，表白成功')

```


#### for循环打印九九乘法表

```python
# 通过外层循环控制行数
for i in range(1, 10):
    # 通过内层循环控制每一行的数量
    for j in range(1, i + 1):
        print(f'{j} * {i} = {j * i}', end='\t')
    print()

```


#### 公司账户余额1万元，给20名员工发工资

- 员工编号1-20依次领取工资1000元
- 领工资时判断员工绩效分(1-10)(随机生成)，低于5不发工资，换下一位
- 如果工资发完了，结束发工资

```python
import random

money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)
    if money < 1000:
        print(f'工资还剩{money}, ❌')
        break
    elif score < 5:
        print(f'员工{i}的绩效分是{score}，❌')
        continue
    else:
        money -= 1000
        print(f'员工{i}✅，满足条件，发放工资1000，公司账户余额{money}')

```


## 函数

案例：黑马ATM  
定义全局变量：money，用来记录银行卡余额(默认5_000_000)  
定义全局变量：name，用来记录客户姓名(启动程序时用)  
定义如下的函数:
1. 查询余额函数
2. 存款函数
3. 取款函数
4. 主菜单函数

要求：
- 程序启动后要求输入客户姓名
- 查询1.2.3.后返回4.
- 2.3.后应显示1.
- 客户选择退出或输入错误程序才会break

```python
# 定义全局变量
money = 5_000_000
# 要求客户输入姓名
name = input('请输入您的姓名：')


# 定义查询函数
def query(show_header):
    if show_header:
        print('-' * 10, '查询余额', '-' * 10)
    print(f'{name}, 您的余额：{money}元')


# 定义存款函数
def saving(n):
    global money  # money在函数内部定义为全局变量
    money += n
    print('-' * 10, '存款', '-' * 10)
    print(f'{name}👋，您存款{n}元成功')
    # 查询
    query(0)


# 定义取款函数
def get_money(n):
    global money  # money在函数内部定义为全局变量
    money -= n
    print('-' * 10, '取款', '-' * 10)
    print(f'{name}👋，您取款{n}元成功')
    # 查询
    query(0)


# 定义主菜单函数
def main():
    print('-' * 10, '主菜单', '-' * 10)
    print(f'{name}👋，欢迎来到🦄️🏧，请选择操作：')
    print(f'查询余额\t[输入1]')
    print(f'存款\t\t[输入2]')  # 通过\t制表符对齐输出
    print(f'取款\t\t[输入3]')
    print(f'退出\t\t[输入4]')
    return input(f'请输入选择: ')


while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query(1)
        continue  # 每次查询、存款、取款后都返回主菜单
    elif keyboard_input == '2':
        num = int(input('您想要存多少钱? '))
        saving(num)
        continue
    elif keyboard_input == '3':
        num = int(input('您想要取多少钱？'))
        get_money(num)
        continue
    else:
        print('程序退出')
        break

```


## 数据容器(序列)

**如果函数定义为class的成员，那么称为方法**

- 列表方法
  - list.index(element)
  - list.insert(index, element)
  - list.extend(其他数据容器)将其他数据容器内容取出，依次追加到列表尾部
  - list.remove(element)
  - list.count(element)

- list遍历

```python
index = 0  
while index < len(list):  
    element = list(index)
    对元素进行process
    element += 1
```

- 元组方法
  - tuple.index(element)
  - tuple.count(element)
  - len(tuple)

元组中的列表内部的元素可以被修改


## 字符串

- 字符串不可被修改
- 字符串方法
  - str.index(item)
  - new_str = str.replace(str1, str2)
  - new_str_list = str.split(separator str)
  - string.count(str)
  - new_str = str.strip()
  - new_str = str.strip(指定的str)
```python
string = '12ranshen21'
new_str = string.strip('12')
传入的'12'其实就是'1'和'2'都会被移除，是按照单个字符
```


## 序列（list, tuple, str)

- 序列方法
  - new_sequence = sequence[:]
  - new_sequence = sequence[::2]


## 集合

- 不支持元素item重复
- 内容无序(不支持index,不能用while，只能用for)
- 使用set()
- 和list一样允许被修改

集合方法：

- set.add(item)
- set.remove(item)
- set.pop()  `随机`
- set.clear()
- `set3 = set1.difference.set2()` set1有，set2没有的
- 消除两个集合的差集
  ```python
  set1 = {1, 2, 3}
  set2 = {1, 5, 6}
  set1.difference_update(set2)  # 集合1被修改，集合2不变
  print(set1)  # 结果：{2, 3}
  print(set2)  # 结果：{1, 5, 6}
  ```
- set3 = set1.union(set2)
- len(set)


可变数据类型：值发生变化，id不变
不可变数据类型：值发生了变化，id也变化


## 字典

- value可以是任意数据类型
- key要求是不可变序列
- 字典无序，不支持❌while循环♻️
- 不存在则添加，存在则更新

#### 字典方法
- dict.pop(key)
- dict.clear()
- dict.keys()
- len(dict)


### 数据容器通用的方法

- len(容器)
- max(容器)
- min(容器)
- list(容器)
- tuple(容器)
- str(容器)
- set(容器)
- sorted(容器, [reverse=True]) `排序结果为列表对象`
- sorted()函数返回重新排序的列表，与sort()函数的区别在于sort()函数是list列表中的函数，而sorted()函数可以对所有可迭代对象进行排序操作。并且用sort()函数对列表排序时会影响列表本身，而sorted()函数则不会。
- index()
- count()
