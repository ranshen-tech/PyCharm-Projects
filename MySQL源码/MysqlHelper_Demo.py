# 教育机构：马士兵教育
# 讲   师：张祖春

from MysqlHelper import *

'''
#查询数据
mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "select sno,sname,sex,age,enterdate,classname from t_student where age>=%s"
params = (19)
result = mysqlhelper.get_all(sql,params)

#打印执行结果
for row in result:
    print(row)'''

'''
#增加数据
mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "insert into t_student values (%s,%s,%s,%s,%s,%s,%s,%s)"
params = (11,"王五","123456",'男',24,"2020-09-15","大数据班","123456@126.com")
rowcount = mysqlhelper.insert(sql,params)

print("已增加"+str(rowcount)+"条数据")'''

'''
#删除数据
mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "delete from t_student where sno=%s"
params = (9)
rowcount = mysqlhelper.delete(sql,params)

print("已删除"+str(rowcount)+"条数据")'''

#修改数据
mysqlhelper = MysqlHelper(MysqlHelper.conn_params1)
sql = "update t_student set sname=%s where sno=%s"
params = ('李军',11)
rowcount = mysqlhelper.update(sql,params)

print("已修改"+str(rowcount)+"条数据")