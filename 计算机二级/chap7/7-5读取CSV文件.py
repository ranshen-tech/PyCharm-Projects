f=open('d:/city.csv','r')
lst=f.read().strip('\n').split(',')
f.close()
print(lst)


