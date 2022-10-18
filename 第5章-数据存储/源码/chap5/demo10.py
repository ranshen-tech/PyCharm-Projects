import mysql.connector

# 创建连接对象
conn = mysql.connector.connect(host='localhost', user='root', passwd='root', database='test',
                               auth_plugin='mysql_native_password')
# print(conn)
mycursor = conn.cursor()
#
# # 编写sql语句
# sql = 'insert into dept (deptno,dname,loc) values (%s,%s,%s)'
# val = (50, '开发部', '北京')
#
# # 执行sql语句
# mycursor.execute(sql, val)
#
# # 提交
# conn.commit()
# print(mycursor.rowcount, '记录插入成功')
