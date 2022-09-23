f=open('D:/cpi.csv','r')
lst=[]
for line in f:
    lst.append(line.strip('\n').split(','))
f.close()
for row in lst:
     line=''
     for item in row:
        line+='{:10}\t'.format(item)
     print(line)


