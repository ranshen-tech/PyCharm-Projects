#教育机构 ：马士兵教育
#讲    师：杨淑娟
#修改
import  mysql.connector
#创建连接对象
conn=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test',auth_plugin='mysql_native_password')
#print(conn)
mycursor=conn.cursor()
#编写sql语句
sql='select * from dept'
#执行查询操作
mycursor.execute(sql)
#获取所有查询的记录
myresult=mycursor.fetchall()
print(type(myresult))
for item in myresult:
    print(item)

