lst=['北京','上海','天津','重庆']
f=open('D:/city.csv','w')
f.write(','.join(lst)+'\n')
f.close()


