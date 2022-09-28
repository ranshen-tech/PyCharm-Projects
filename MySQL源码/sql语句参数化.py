# 教育机构：马士兵教育
# 讲   师：张祖春

#1  导入pymsql包
from pymysql import *

#2 创建数据库连接
conn = connect(host='localhost',port=3306,user='root',password='root',db='mytestdb',charset='utf8')

#3 打开游标
cur = conn.cursor()

#4 执行 sql语句
# 让用户输入用户名密码
sname = input("请输入用户名：")
passwd = input("请输入密码：")

# 编写sql语句
sql = "select * from t_student where sname=%s and passwd=%s"
params = (sname,passwd)

# 执行sql语句，返回查询到的记录条数rowcount,如果rowcount不为0，则登录成功，否则登录失败
rowcount = cur.execute(sql,params)

if rowcount!=0:
    print("登录成功")
else:
    print("登录失败")

#5 关闭游标
cur.close()

#6 关闭连接
conn.close()