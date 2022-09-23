import random
lst1=[chr(i) for i in range(97,123)] #26个字母的列表

lst2=[i for i in range(0,10)] #10个数字的列表


result=lst1+lst2  #拼接两个列表

for i in range(10):
    for j in range(8):
        print(random.choice(result),end='')
    print()


