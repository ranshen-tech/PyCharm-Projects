import jieba

lst = jieba.cut('Python是最有意思的编程语言')
lst = list(lst)
print(lst)
