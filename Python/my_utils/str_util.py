# def str_reverse(s):
#     """
#     将接收的字符串反转返回
#     :param s: str
#     :return: str
#     """
#     return ''.join(sorted(s, reverse=True))


def str_reverse(s):
    """
    将接收的字符串反转返回
    :param s: str
    :return: str
    """
    return s[::-1]


def sub_str(s, x=0, y=len(s)):
    """
    按照下标x, y对传入的字符串切片
    :param s: str
    :param x: int
    :param y: int
    :return: str
    """
    return s[x: y]


if __name__ == '__main__':
    print(str_reverse('黑马程序员'))
    print(sub_str('黑马程序员', 1, 3))
