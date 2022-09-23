s=eval(input('请输入一个整数'))
result='' if s%3==0 and s%5==0 else '不'
print('这个数字{}能够同时被3和5整数'.format(result))
