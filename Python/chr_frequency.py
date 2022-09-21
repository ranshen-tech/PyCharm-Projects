"""
英文字符频率统计：对给定字符中出现的a-z字母频率进行分析，忽略大小写，采用降序输出
"""
# TODO 可以改进
# txt = input('please enter a text in English: ')
# txt = txt.lower()
# counts = {}  # 存储字母与个数的键值对
# lst = [chr(i) for i in range(97, 123)]
# for i in txt:
#     if i in lst:
#         counts[i] = counts.get('i', 0) + 1
# items = list(counts.items())
# print(items)
# items.sort(key=lambda x: x[1], reverse=True)
# print(items)
# for i in range(len(items)):
#     word, count = items[i]
#     print(word, count)


"""
含中文字频统计
"""
# txt = input('please enter a text in English: ')
# d = {}
# for i in txt:
#     d[i] = d.get(i, 0) + 1  # 计数
# lst = list(d.items())
# lst.sort(key=lambda x: x[1], reverse=True)  # 排序
# for i in range(len(lst)):
#     word, count = lst[i]
#     print(f'{word}, {count}')
