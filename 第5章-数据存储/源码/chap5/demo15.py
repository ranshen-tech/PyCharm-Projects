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

#修改操作 一次修改一条数据
#collection.update_one({'name':'李四'},{'$set':{'age':20}})

collection.update_many({'name':'麻七'},{'$set':{'gender':'男'}})
