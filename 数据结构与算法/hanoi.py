# def hanoi(n, a, b, c):
#     """:param n: n个石盘
#     :param a: 石柱a
#     :param b: 石柱b
#     :param c: 石柱c"""
#     if n > 0:
#         hanoi(n - 1, a, c, b)
#         print(f'moving from {a} to {c}')
#         hanoi(n - 1, b, a, c)




hanoi(2, "A", "B", "C")
