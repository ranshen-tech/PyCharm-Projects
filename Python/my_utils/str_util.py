def str_reverse(s):
    """
    将接收的字符串反转返回
    :param s: str
    :return: str
    """
    return ''.join(sorted(s, reverse=True))


def sub_str(s, x, y):
    """
    按照下标x, y对传入的字符串切片
    :param s: str
    :param x: int
    :param y: int
    :return: str
    """
    return s[x: y]


if __name__ == '__main__':
    print(str_reverse('123'))
    print(sub_str('ran0519', 2, 4))
