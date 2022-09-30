# def hanoi(n, a, b, c):
#     """
#     汉诺塔问题
#     :param n: n个石盘
#     :param a: 石柱a
#     :param b: 石柱b
#     :param c: 石柱c
#     """
#     if n > 0:
#         hanoi(n - 1, a, c, b)
#         print(f'moving from {a} to {c}')
#         hanoi(n - 1, b, a, c)


# def linear_search(ls, value):
#     """
#     线性查找
#     :param ls: list
#     :param val: 要查找的值
#     """
#     for i, v in enumerate(ls):
#         if v == value:
#             return i
#     else:
#         return None


def binary_search(ls, value):
    left = 0
    right = len(ls) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if ls[mid] == value:
            return mid
        elif value < ls[mid]:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # mid < value 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(lst, 5))
