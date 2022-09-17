"""
1、录入5个商品信息（编号、名称）添加到购物列表
2、展示商品信息
3、提示用户选择商品
4、用户选中的商品添加到购物车🛒（如果不存在要有相应提示）
"""
# 创建商品列表
lst = []
for _ in range(5):
    goods = input('请输入商品的编号和名称(1手机)，每次只能输入一件： ')
    lst.append(goods)
# 输出所有商品信息💻
for item in lst:
    print(item)
# 创建购物车（cart）列表
cart = []
while True:
    num = input('请输入要购买的商品编号(退出按q）：')
    # 遍历商品列表，查询购买商品是否存在
    for item in lst:
        if num == lst[0]:
            cart.append(item)
            print('以成功添加到购物车')
            break  # 退出的是for循环♻️
    if num == 'q':
        break  # 退出的是while循环
print('您购物车选中的商品')
for item in cart:
    print(item)
