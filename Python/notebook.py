"""
2022-09-18

"""
# 字符串驻留机制：拼接🪢和修改字符串影响性能；用join代替拼接'+'
# ord() chr() 请你猜猜我的名字
# s = 'ranshen'
# print(s.count('n', 1))

# 字符串编码/解码
# s = '冉申'
# es = s.encode(encoding='utf-8')
# print(es)
# print(type(es))
# ds = es.decode(encoding='utf-8')
# print(ds)
# print(type(ds))

# 字符串格式化
# name = '冉申'
# age = 18
# print('姓名%s, 年龄%d' % (name, age))
# print('姓名{}, 年龄{}'.format(name, age))
# print(format())


# 身份证号自动识别出身日期（提供N个身份证号，提取年月日）


# 取余运算
# 17(被除数) / (-3)(除数) = -6(商)······-1(余数)
# 被除数 = 除数 * 商 + 余数
# 商 = (被除数 - 余数) / 除数
# 余数是除法的商向小取整，余数符号同被除数
# print(17 % -3)  # 商-6 余-1
# print(-17 % 3)  # 商-6 余1
# print(-17 % -3)  # 商 -5 余-2
