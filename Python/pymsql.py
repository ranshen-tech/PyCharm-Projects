"""
演示pymysql库的基本操作
"""

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,  # 端口
    user='root',  # 账户
    password='ranshen0519',  # 密码
    autocommit=True  # 设置自动提交
)
# 执行非查询性质SQL
cursor = conn.cursor()  # 获取到游标对象
# 选择数据库
conn.select_db("ranshen")
# 执行SQL
# cursor.execute("create table test_pymysql_2(id int)")
cursor.execute('select * from student')
# cursor.execute("insert into student values(10002, '林俊杰', 31, '男')")
# # 通过commit确认
# conn.commit()
results: tuple = cursor.fetchall()
# print(results)
for i in results:
    print(i)
# 关闭链接
conn.close()
