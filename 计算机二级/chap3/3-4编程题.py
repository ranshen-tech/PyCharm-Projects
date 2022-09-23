x = input("input a number:n")
flag=True
for i in range(len(x)//2):
    if x[i] != x[-i - 1]:
        print('this number is not a huiwen')
        flag=False
        break
if flag:
    print ('this number is a huiwen')
