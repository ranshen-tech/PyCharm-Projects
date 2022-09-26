"""
和文件相关的类定义
"""


# 定义一个抽象类做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们封装到list内返回"""
        pass
