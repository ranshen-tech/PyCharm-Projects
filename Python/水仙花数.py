# 100-999之间的水仙花数
"""
153
3**3 + 5**3 + 1**3 = 27 + 125 + 1 = 153
"""
for i in range(100, 1000):
    units = i % 10
    tens = i // 10 % 10
    hundreds = i // 100
    if units ** 3 + tens ** 3 + hundreds ** 3 == i:
        print(i)
