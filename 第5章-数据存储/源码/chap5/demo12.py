#教育机构 ：马士兵教育
#讲    师：杨淑娟
#修改
import  mysql.connector
#创建连接对象
conn=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test',auth_plugin='mysql_native_password')
#print(conn)
mycursor=conn.cursor()
#编写SQL语句
#sql='update dept set dname="Python部门" where deptno=50'
sql='delete from dept where deptno=80'
#执行SQL语句
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount,'删除成功')
