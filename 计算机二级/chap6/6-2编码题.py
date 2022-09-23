txt = input("请输入一段文本：")
d = {}
for i in txt:
    d[i] = d.get(i,0) + 1                    # 字典中的值

    
ls = list(d.items())

ls.sort(key = lambda x:x[1],reverse = True)  # 排序用的

for i in range(len(d)):
    
    word,count = ls[i]
    
    print("{:<10}{:<5}".format(word,count))

    
