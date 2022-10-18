#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  mysql.connector
#创建连接对象
conn=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test',auth_plugin='mysql_native_password')
#print(conn)
mycursor=conn.cursor()

#编写sql语句
sql='insert into dept (deptno,dname,loc) values (%s,%s,%s)'

vals=[
    (60,'财务部','上海'),
    (70,'测试部','长春'),
    (80,'市场部','深圳')
]
mycursor.executemany(sql,vals)

conn.commit()
print(mycursor.rowcount,'记录插入成功')




