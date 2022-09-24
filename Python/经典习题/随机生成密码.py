"""
使用random库，采用0x1010作为随机种子
密码：abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
密码长度10字符
程序每次产生10个密码，每个密码一行
随机产生的密码保存在'随机密码.txt'文件中
"""
# print(chr(0x1010))  # 无限♾️
import random
random.seed(0x1010)
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
lst = []
excludes = ''  # 用于首位排除

while len(lst) < 10:  # 产生十个密码
    passwords = ''
    for i in range(10):  # 产生十位密码
        passwords += s[random.randint(0, len(s) - 1)]
    if passwords[0] in excludes:
        continue
    else:
        lst.append(passwords)
        excludes += passwords[0]

# 存储
with open('随机密码.txt', 'w') as fw:
    fw.write('\n'.join(lst))

