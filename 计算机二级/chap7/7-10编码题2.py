f=open('demo.txt','r')
s=f.readlines()
f.close() #读取内容结束

r=[i.swapcase() for i in s]
print(r)

#转换后写入
f =open('demo1.txt','a+')
f.writelines(r)
f.seek(0)
ss=f.read()
f.close()

print('转换后的结果为:',ss)

