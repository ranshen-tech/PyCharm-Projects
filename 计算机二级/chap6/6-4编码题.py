def if_repeat(lst):
    n=input('请输入要判断的元素：')
    lst2=lst.copy()
    if n in lst2:
        lst2.remove(n)
        if n in lst2:
            print(True)
        else:
            print(False)
    else:
        print(False)

lst=list(input('请输入元素，以空格分隔').split(' '))

if_repeat(lst)
print(lst)


