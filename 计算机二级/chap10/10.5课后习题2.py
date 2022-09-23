import jieba
jieba.add_word('意大利面')
lst=jieba.cut('今天晚上我吃了意大利面')
lst=list(lst)
print(lst)


