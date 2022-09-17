### 赋值
- **链式赋值**
`a = b = c = 100`
- **交换赋值**
`a, b = b, a`

## 函数

案例：黑马ATM  
全局变量：money，记录银行卡余额(默认5_000_000)  
全局变量：name，用录客户姓名(启动程序时用)  
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
