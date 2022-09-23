f=open('D:/cpi.csv','r')
lst=[]
for line in f:
    lst.append(line.strip('\n').split(','))
f.close()
print(lst)


