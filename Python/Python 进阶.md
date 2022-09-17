### 函数的多返回值

### 函数的多种传参方式

- **位置参数**：
  - 调用函数时根据`函数定义的参数位置`来传递参数
- **关键字参数**：函数调用时根据`键=值`的形式传入参数

```python
# 可以和位置参数混用
def user_info(name, age, gender):
    print(f'姓名是：{name}，年龄是：{age}， 性别是：{gender}')


user_info(name='rs', age=30, gender='男')
```

- **缺省参数(默认参数)**: 用于定义参数，为参数提供默认值。`所有位置参数必须出现在默认参数前`
```python
def user_info(name, age, gender='female'):
    print(f'姓名是：{name}，年龄是：{age}， 性别是：{gender}')


user_info('ranshen', 33, 'male')

```

- **不定长参数(可变参数)**: 用于`不确定调用的时候会传递多少个参数`的场景
  - 位置传递
```python
def user_info(*args):
    print(f'user_info参数的类型是：{type(args)}, 内容是：{args}')


user_info('ran')  # user_info参数的类型是：<class 'tuple'>, 内容是：('ran',)
user_info('ran', 18)  # user_info参数的类型是：<class 'tuple'>, 内容是：('ran', 18)
```
  - 关键字传递: 参数是`'键=值'`形式的情况下，所有`'键=值'`都会被kwargs接受，同时会根据`'键=值'`组成`字典`
```python
def user_info(**kwargs):
    print(f'user_info参数的类型是：{type(kwargs)}, 内容是：{kwargs}')


user_info(name='ran', age=18, id=110)  # user_info参数的类型是：<class 'dict'>, 内容是：{'name': 'ran', 'age': 18, 'id': 110}
user_info(gender='male')  # user_info参数的类型是：<class 'dict'>, 内容是：{'gender': 'male'}
```


### 匿名函数

- 函数作为参数传递的方式
- lambda函数：`lambda 参数: 函数体`
  - 无法重复调用
  - 无法写多行
```python
def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

# <class 'function'>
# 3
test_func(lambda x, y: x + y)
```
