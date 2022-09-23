f=open('cpi.csv','r')
data=[]
for item in f:
    lst=item.strip('\n').split(',')
    data.append(lst)
#print(data)

for row in data:
    for col in row:
        print('{:10}'.format(col),end=' ')
    print()

f.close()
