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
excludes = ''
