__author__ = 'ranshen0519@icloud.com'
from random import randint


# 选手类
class Player:
    # 每当创建新对象，都自动为他登记信息
    def __init__(self, name, hp, atk):
        self.name = name  # 为选手登记姓名
        self.hp = hp  # 为选手登记生命值
        self.atk = atk  # 为选手登记攻击力
        print('已成功登记信息')
        self.show_info()

    # 展示信息
    def show_info(self):
        print(f'+ {self.name}\tHP: {self.hp}\tATK: {self.atk}\n')

    # 发动攻击
    def hit(self, target):
        print(f'>> 【{self.name}】向【{target.name}】发动攻击，\n')
        target.defend(self.atk)

    # 防御攻击
    def defend(self, damage):
        if randint(1, 100) <= 20:
            print(f'>> 【{self.name}】完美躲避了攻击！\n')
        else:
            self.hp -= damage
            print(f'>> 【{self.name}】收到了{damage}点伤害...\n')


# 实例化 Player 类，生成一个新的实例对象，赋值给变量 kakarot
kakarot = Player('卡卡罗特', 100, 25)
# 实例化 Player 类，生成一个新的实例对象，赋值给变量 piccolo
piccolo = Player('比克大魔王', 120, 20)
# 展开决斗
while True:
    # 每回合开始，由卡卡罗特先发动攻击
    kakarot.hit(piccolo)
    # 判断此时决斗是否分出胜负
    if piccolo.hp <= 0:
        print(f'\n{kakarot.name}获胜！')
        break
    # 若未分出胜负，则攻防交换，由比克大魔王发动攻击
    piccolo.hit(kakarot)
    # 判断此时决斗是否分出胜负
    if kakarot.hp <= 0:
        print(f'\n{piccolo.name}获胜！')
        break
    # 每回合结束，打印出两人当前信息
    kakarot.show_info()
    piccolo.show_info()
    print(f'{"-" * 32}\n')
