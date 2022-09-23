import jieba

with open('天龙八部-网络版.txt') as f:
    with open('天龙八部-词语统计.txt', 'w') as fw:
        txt = jieba.lcut(f.read().replace(' ', '').replace('\n', '').replace('。', ''))
        d = {}
        for word in txt:
            d[word] = d.get(word, 0) + 1
        lst = []
        for key in d:
            lst.append(f'{key}: {d[key]}')
        fw.write(','.join(lst))

