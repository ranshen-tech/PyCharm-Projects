def if_repeat(lst):
    """
    接收列表作为参数，如果重复出现，返回True
    :param lst: list
    :return: bool
    """
    elem = input('请输入要判断的element: ')
    if elem in lst:
        lst.remove(elem)
        if elem in lst:
            print('True')
        else:
            print('False')
    else:
        print('False')


txt = list(input('请输入元素：'))
if_repeat(txt)
print(txt)
