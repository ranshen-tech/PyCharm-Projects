num = int(input('请输入四位数：'))
units = num % 10  # 个位上的数
tens = num // 10 % 10  # 十位上的数
hundreds = num // 100 % 10  # 百位上的数
thousands = num // 1000  # 千位上的数
print(f'个位数：{units}')
print(f'个位数：{tens}')
print(f'个位数：{hundreds}')
print(f'个位数：{thousands}')
