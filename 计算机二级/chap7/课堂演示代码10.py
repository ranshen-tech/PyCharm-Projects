f=open('city.csv','r')
lst=f.read().strip('\n').split(',')
print(lst,type(lst))
f.close()
