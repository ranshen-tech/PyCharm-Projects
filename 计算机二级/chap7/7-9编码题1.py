def times(filename,char):
    count=0
    with open(filename,'r',encoding='utf-8') as file:
        txt=file.read()
        txt=txt.lower()
        for w in txt:
            if char==w:
                count+=1
    return count

print(times('b.txt','w'))


