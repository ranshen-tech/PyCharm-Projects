value=input('请向列表中添加第1个元素')
num=1
lst=[]
lst.append(value)
while value!='':
    num+=1
    value=input('请向列表添加第{}个元素，按空格结束'.format(num))
    lst.append(value)
#将逗号换成.
for i in range(len(lst)):
    if ',' ==lst[i]:
        lst[i]=lst[i].replace(',','.')
#保存
f=open('a.csv','w',encoding='utf-8')
f.write(','.join(lst)+'\n')
f.close() #

print('csv文件保存完成!!!')
#读取
f2=open('a.csv','r',encoding='utf-8')
data=f2.read().strip('\n').split(',')
for i in range(len(data)):
    if '.' == data[i]:
        data[i]=data[i].replace('.',',')
print(data)
f2.close()

    
    
