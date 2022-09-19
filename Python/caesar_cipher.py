"""
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
plain_text = input('plain text: ')
key = int(input('key: '))  # 位移长度（密匙🔑）
for letter in plain_text:
    if 'a' <= letter <= 'z':
        # o就是ord数字的意思
        o = ord('a') + (ord(letter) - ord('a') + key) % 26
        print(chr(o), end='')
    elif 'A' <= letter <= 'Z':
        o = ord('A') + (ord(letter) - ord('A') + key) % 26
        print(chr(o), end='')
    else:
        print(letter, end='')
print()


# 解锁🔓
cypher_text = input('cypher text: ')
key = int(input('key: '))
for letter in cypher_text:
    if 'a' <= letter <= 'z':
        o = ord('a') + (ord(letter) - ord('a') - key) % 26
        print(chr(o), end='')
    elif 'A' <= letter <= 'Z':
        o = ord('A') + (ord(letter) - ord('A') - key) % 26
        print(chr(o), end='')
    else:
        print(letter, end='')
