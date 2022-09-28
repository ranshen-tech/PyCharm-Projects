# 教育机构：马士兵教育
# 讲   师：张祖春

# 1  导入pymsql包
from pymysql import *

# 2 创建数据库连接
conn = connect(host='localhost', port=3306, user='root', password='root', db='mytestdb', charset='utf8')

# 3 打开游标
cur = conn.cursor()

# 4 执行 sql语句
# 编写sql语句

# 查询数据进，为了节约内存，不要用*，而应指定具体需取的字段，另外要指定查询条件，限制查询条数
sql = "select sno,sname,sex,age,enterdate,classname from t_student where age>=%s"
params = (19)
# 执行sql语句
cur.execute(sql, params)

# result = cur.fetchone() #取一条数据
# print(result)

result = cur.fetchall()  # 取所有数据

for row in result:
    print(row)

# 5 关闭游标
cur.close()

# 6 关闭连接
conn.close()
