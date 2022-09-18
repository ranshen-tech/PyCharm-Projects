def print_file_into(file_name):
    """
    :param file_name: 文件路径
    :return: 打印文件全部内容，如文件不存在则打印异常，输出提示信息，用finally关闭文件对象
    """
    try:
        f = open(file_name)
    except Exception as e:
        print(e)
        print('文件不存在')
    else:
        print(f.read())
    # finally:
        f.close()


def append_to_file(file_name, data):
    """
    将数据追加写入到文件中
    :param file_name: 文件路径
    :param data: 传入数据
    :return:
    """
    f = 0
    with open(file_name, 'a', encoding='UTF-8') as f:
        f.write(data)


if __name__ == '__main__':
    print_file_into('inexistence.txt')
    append_to_file('inexistence.txt', 'i love u')
