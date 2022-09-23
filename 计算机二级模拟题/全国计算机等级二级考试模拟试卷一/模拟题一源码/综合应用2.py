fi=open('论语-提取版.txt','r',encoding='utf-8')
fo=open('论语-原文.txt','w',encoding='utf-8')

for item in fi:
   for i in range(1,31):
       item=item.replace('({})'.format(i),'')

   fo.write(item)
fi.close()
fo.close()
