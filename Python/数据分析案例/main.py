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

text_file_reader = TextFileReader('2011年1月销售数据.txt')
json_file_reader = JsonFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并成一个list存储
all_data: list[Record] = jan_data + feb_data

# 进行数据计算

