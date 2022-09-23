PATH='D:/'
file=open(PATH+'bar.txt','rt') #D:/bar.txt
for line in file:
    print(line)
file.close()
