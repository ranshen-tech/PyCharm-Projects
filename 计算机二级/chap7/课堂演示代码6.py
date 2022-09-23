PATH='D:/'
file=open(PATH+'bar.txt','rt') #D:/bar.txt
print(file.read())
print('-------------')
file.seek(0)
print(file.readlines())
file.close()
