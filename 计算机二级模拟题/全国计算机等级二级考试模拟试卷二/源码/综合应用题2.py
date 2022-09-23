import jieba
fi=open('天龙八部-网络版.txt','r',encoding='utf-8')
fo=open('天龙八部-词语统计.txt','w',encoding='utf-8')
txt=fi.read()
txt=jieba.lcut(txt)
#print(len(txt))
d={}
for word in txt:
    d[word]=d.get(word,0)+1

lst=[]
for key in d:
    lst.append('{}:{}'.format(key,d[key]))

fo.write(','.join(lst))
fi.close()
fo.close()
