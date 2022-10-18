#教育机构 ：马士兵教育
#讲    师：杨淑娟
#JSON数据的存储
import json
s='{"name":"张三"}'

#将字符串转成对象
obj=json.loads(s)
print(type(obj))
print(obj)

#将对象转成字符串类型
ss=json.dumps(obj,ensure_ascii=False)
print(type(ss))
print(ss)

#把对象(dict)保存到文件中
json.dump(obj,open('movie.txt','w',encoding='utf-8'),ensure_ascii=False)

#把文件中的内容读取到Python程序
obj2=json.load(open('movie.txt',encoding='utf-8'))
print(obj2)
print(type(obj2))
