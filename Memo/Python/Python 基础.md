- **链式赋值**
`a = b = c = 100`
- **交换赋值**
`a, b = b, a`
- 列表方法
  - list.index(element)
  - list.insert(index, element)
  - list.extend(其他数据容器)将其他数据容器内容取出，依次追加到列表尾部
  - list.remove(element)
  - list.count(element)
- 元组方法
  - tuple.index(element)
  - tuple.count(element)
  - len(tuple)
- 字符串方法
  - str.index(item)
  - new_str = str.replace(str1, str2)
  - new_str_list = str.split(separator str)
  - string.count(str)
  - new_str = str.strip()
  - new_str = str.strip(指定的str)
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
