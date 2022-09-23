s=input('请输入一个小数:')
n=''
i=0
while i<len(s):
    if s[i]=='.':
        n=s[:i]
    i=i+1

print(n)
