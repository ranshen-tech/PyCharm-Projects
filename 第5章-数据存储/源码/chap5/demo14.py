# 教育机构 ：马士兵教育
# 讲    师：杨淑娟

import pymongo

# 连接服务器
client = pymongo.MongoClient('localhost', 27017)

# 获取要操作的数据库
# db=client.school
db = client['school']

# 获取要操作的集合
# collection=db.student
collection = db['student']

# 插入操作
# stu={'name':'张一一','age':20,'gender':'女'}
# collection.insert_one(stu)

# 一次插入多条数据
lst = [
    {'name': '王二二', 'age': 23},
    {'name': '张三三', 'gender': '男'},
    {'name': '枙四四', 'age': 24}
]
collection.insert_many(lst)
