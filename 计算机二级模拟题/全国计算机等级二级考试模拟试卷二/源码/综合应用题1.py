"""
问题1：请编写程序，对《天龙八部》文本中出现的汉字和标点符号进行统计
字符与出现次数之间用冒号分隔，输出保存以“天龙八部-汉字统计.txt”文件中
该文件要求使用CSV格式存储，参数格式如下（注意，不统计空格和回车字符）
"""

with open('天龙八部-网络版.txt') as f:
    with open('天龙八部-汉字统计.csv', 'w') as fw:
        txt = f.read().strip()
        d = {}
        for i in txt.replace(' ', '').replace('\n', ''):
            d[i] = d.get(i, 0) + 1
        lst = []
        for key in d:
            lst.append(f"{key}: {d[key]}")
        fw.write(','.join(lst))

