#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  pymongo
#连接服务器
client=pymongo.MongoClient('localhost',27017)

#获取要操作的数据库
#db=client.school
db=client['school']

#获取要操作的集合
#collection=db.student
collection=db['student']

#查询全部数据
result=collection.find()
for item in result:
    print(item)
print('--------------------------------')
result=collection.find({'name':'麻七'})
for item in result:
    print(item)
print('--------------------------------')

result=collection.find({'name':{'$regex':'.*二.*'}})
for item in result:
    print(item)
print('--------------------------------')
#result=collection.find().sort('age',pymongo.ASCENDING)
result=collection.find().sort('age',pymongo.DESCENDING)
for item in result:
    print(item)
print('--------------------------------')
result=collection.find().sort('age',pymongo.DESCENDING).limit(3)
for item in result:
    print(item)
print('--------------------------------')
result=collection.find().sort('age',pymongo.DESCENDING).skip(3).limit(3)
for item in result:
    print(item)
print('--------------------------------')