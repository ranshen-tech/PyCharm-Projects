lst=['北京','上海','重庆','天津']
f=open('city.csv','w')
f.write(','.join(lst)+'\n')
f.close()
