lst1=list(input('请输入元素').split(' '))
if lst1!=list(set(lst1)):
    print(True)
else:
    print(False)
    
print(list(set(lst1)))

print(lst1)


