# 教育机构：马士兵教育
# 讲   师：张祖春

#1  导入pymsql包
from pymysql import *

#2 创建数据库连接
conn = connect(host='localhost',port=3306,user='root',password='root',db='mytestdb',charset='utf8')

#3 打开游标
cur = conn.cursor()

#4 执行 sql语句
pass

#5 关闭游标
cur.close()

#6 关闭连接
conn.close()