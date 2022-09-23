txt=input('请输入一段英文文本:')
txt=txt.lower() #转小写
counts={} #用于存储字母与个数的键值对

lst=[chr(i) for i in range(97,123)]

print(lst)

for i in txt:
    if i in lst:
        counts[i]=counts.get(i,0)+1
items=list(counts.items())


items.sort(key=lambda x:x[1],reverse=True)

for i in range(len(items)):
    word,count=items[i]
    print(word,count)

    
