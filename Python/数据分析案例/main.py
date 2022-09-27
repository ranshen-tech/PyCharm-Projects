"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，生产数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
"""
from file_define import FileReader, JsonFileReader, TextFileReader
from data_define import Record
from pyecharts.charts import Bar  # 构建柱状图对象
from pyecharts.options import *  # 构建可选的选项
from pyecharts.globals import ThemeType  # 导入主题，控制图标颜色
from pymysql import Connection

text_file_reader = TextFileReader('2011年1月销售数据.txt')
json_file_reader = JsonFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并成一个list存储
all_data: list[Record] = jan_data + feb_data
# 进行数据计算
# {"2011-01-01": 1234, "2011-01-02": 300, "2011-01-03": 650}
# data_dict = {}
# for record in all_data:
#     if record.date in data_dict.keys():
        # 当前日期已经有记录了，和旧记录累加即可
        # data_dict[record.date] += record.money
    # else:
    #     data_dict[record.date] = record.money

# print(data_dict)


# 可视化图标开发
# bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
# bar.add_xaxis(list(data_dict.keys()))  # 添加x轴数据
# bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 添加了y轴数据
# 给当前图表设置标题
# bar.set_global_opts(
#     title_opts=TitleOpts(title="每日销售额")
# )
# bar.render("每日销售额柱状图.html")


# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="ranshen0519",
    autocommit=True
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)
# 关闭MySQL链接对象
conn.close()
