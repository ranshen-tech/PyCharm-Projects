# 录入5位好友姓名和电话
"""
因为通讯录是无序的，可以用集合来实现
"""
phones = set()
for i in range(1, 6):
    phone_num = input(f'请录入第{i}位好友的手机号码: ')
    # 添加到集合中
    phones.add(phone_num)
# 遍历集合
for item in phones:
    print(item)
