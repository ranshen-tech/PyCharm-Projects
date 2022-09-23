import random
f=open('dx.txt','w')
for line in range(10):
    word=''
    for row in range(10):
        word+=str(random.randint(1,100))+' '
    f.write(word+'\n')
f.close()



#读取文件内容
f1=open('dx.txt','r')
f2=open('dx.csv','w')
for line in f1:
    s=line.replace(' ',',')
    f2.write(s)
f2.close()
f1.close()
