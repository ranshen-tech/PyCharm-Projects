# 人机对战
"""
1：石头
2：剪刀
3：布
电脑出拳：random.randint(1, 3)
"""
import random


while True:
    computer = random.randint(1, 3)
    rs = int(input(': '))
    if computer == 1 and rs == 2 or computer == 2 and rs == 3 or computer == 3 and rs == 1:
        print(f'rs: {rs}, computer: {computer}')
        print('computer win')
    elif computer == 1 and rs == 3 or computer == 2 and rs == 1 or computer == 3 and rs == 2:
        print(f'rs: {rs}, computer: {computer}')
        print('rs win')
    else:
        print(f'rs: {rs}, computer: {computer}')
        print('draw')
    answer = input('y/n: ')
    if answer == 'n':
        break
