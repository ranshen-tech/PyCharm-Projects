

# with open('天龙八部-网络版.txt') as f:
#     with open('天龙八部-汉字统计.txt', 'w') as fw:
#         txt = f.read()
#         d = {}
#         for i in txt:
#             d[i] = d.get(i, 0) + 1
#         lst = []
#         for key in d:
#             lst.append(f"{key}: {d[key]}")
#         fw.write(','.join(lst))


with open('ran.txt') as f:
    # with open('ran1.txt', 'w') as fw:
    txt = f.read()
    a = txt.strip()
    print(a)
        # d = {}
        # for i in txt:
        #     d[i] = d.get(i, 0) + 1
        # lst = []
        # for key in d:
        #     lst.append(f'{key}: {d[key]}')
        # fw.write(','.join(lst))
