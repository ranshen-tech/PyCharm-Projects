fi=open('天龙八部-网络版.txt','r',encoding='utf-8')
fo=open('天龙八部-汉字统计.txt','w',encoding='utf-8')
txt=fi.read()
d={}
for c in txt:
    d[c]=d.get(c,0)+1
lst=[]
for key in d:
    lst.append('{}:{}'.format(key,d[key]))

fo.write(','.join(lst))
fi.close()
fo.close()
