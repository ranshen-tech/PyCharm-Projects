"""
Caesar cypher (第一版)
原文字符P，加密文字符C满足如下条件：
C = (P + 3) mod 26
P = (C - 3) mod 26
对字母a-z和A-Z按照加密算法转换，非英文字母部分直接输出
"""
# print(ord('a'))
# print(97 % 26)
# print(ord('z'))
# print(125 % 26)


# 加密🔐
# plain_text = input('plain text: ')
# key = int(input('key: '))  # 位移长度（密匙🔑）
# for letter in plain_text:
#     if 'a' <= letter <= 'z':
#         # o就是ord数字的意思
#         o = ord('a') + (ord(letter) - ord('a') + key) % 26
#         print(chr(o), end='')
#     elif 'A' <= letter <= 'Z':
#         o = ord('A') + (ord(letter) - ord('A') + key) % 26
#         print(chr(o), end='')
#     else:
#         print(letter, end='')
# print()


# 解锁🔓
# cypher_text = input('cypher text: ')
# key = int(input('key: '))
# for letter in cypher_text:
#     if 'a' <= letter <= 'z':
#         o = ord('a') + (ord(letter) - ord('a') - key) % 26
#         print(chr(o), end='')
#     elif 'A' <= letter <= 'Z':
#         o = ord('A') + (ord(letter) - ord('A') - key) % 26
#         print(chr(o), end='')
#     else:
#         print(letter, end='')


"""
Caesar cypher (第二版)
进一步使用字母表循环左移13位(a左移13位是n，n又移13位是a)
因为一共是26个英文字母，所以既可以加密，又可以解密
"""
# print(chr(65))
# print(chr(97))

# todo 只能输入小写，大写就对不上
s1 = 'abcdefghijklmnopqrstuvwxyz'
s2 = 'nopqrstuvwxy`abcdefghijklz'
d = {}
for letter in range(65, 97):  # chr(65) --> 'A', chr(97) --> 'a'
    for i in range(26):
        d[chr(letter + i)] = chr(letter + (i + 13) % 26)
print(''.join(d.get(letter, letter) for letter in s1))  # 编码
print(''.join(d.get(letter, letter) for letter in s2))  # 解码
# print(ord('_'))
# print(chr(122))
# print(d)

