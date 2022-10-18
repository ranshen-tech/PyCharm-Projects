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

#删除操作
#一次删除一条数据
#collection.delete_one({'name':'张三'})

#一次删除多条数据
collection.delete_many({'age':20})
