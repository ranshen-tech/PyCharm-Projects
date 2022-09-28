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
try:
    # 删除和修改操作一定要限定条件，不然将影响其他数据，甚至误删整个表的数据
    sql = "update t_student set sname=%s where sno=%s"
    params = ('李敏', 8)
    # 执行sql语句
    rowcount = cur.execute(sql, params)
    conn.commit()
except:
    conn.rollback()

print("已修改" + str(rowcount) + "条数据!")
# 5 关闭游标
cur.close()

# 6 关闭连接
conn.close()
