# CaesarEncodeAndDecode.py

s='My name is Yang Shujuan'
s2='Zl anzr vf Lnat Fuhwhna'
d={}
for c in (65,97):
    for i in range(26):
        d[chr(i+c)]=chr((i+13)%26+c)

print(''.join(d.get(c,c) for c in s ))#编码
print(''.join(d.get(c,c) for c in s2 ))#解码


