# 倒三角形
"""
*****
****
***
**
*
"""
for i in range(5):
    for j in range(5 - i):
        print('*', end='')
    print()
print('\n')

# 九九乘法表三角形
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
print('\n')

# 等腰三角形
'''
&&&&*
&&&***
&&*****
&*******
*********
'''
for i in range(5):
    for j in range(4 - i):
        print('&', end='')
    print('*' * (2 * i + 1))
˚
