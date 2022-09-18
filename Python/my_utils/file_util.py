def print_file_into(file_name):
    """
    打印文件全部内容，如文件不存在则打印异常，输出提示信息，用finally关闭文件对象
    :param file_name: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
    except Exception as e:
        print(f'程序出现异常了，原因是：{e}')
    else:
        content = f.read()
        print('文件全部内容如下：')
        print(content)
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    将数据追加写入到文件中
    :param file_name: 文件路径
    :param data: 传入数据
    :return: None
    """
    with open(file_name, 'a', encoding='UTF-8') as f:
        f.write(f'{data}\n')


if __name__ == '__main__':
    print_file_into('inexistence.txt')
    append_to_file('inexistence.txt', 'ran shen')
