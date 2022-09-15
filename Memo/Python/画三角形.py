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


# 菱形
"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
top = int(input('请输入菱形上半部分有多少行：'))
bot = top - 1

for i in range(top):
    for j in range(bot - i):
        print(' ', end='')
    print('*' * (1 + 2 * i))

for i in range(bot):
    for j in range(i + 1):
        print(' ', end='')
    print('*' * (2 * (bot - i) - 1))
