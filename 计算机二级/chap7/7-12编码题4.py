import jieba
fo= open('x.py',"r",encoding='utf-8').read()
table=["def","for","in","return","print","range"]
words  = jieba.lcut(fo)
fo2=open('y.py',"w")
pas=''
for i in range(0,len(words)):
    if words[i] in table:
        continue
    else:
        words[i]=words[i].upper()
        pas="".join(words)
fo2.write(pas)
fo2.close()

