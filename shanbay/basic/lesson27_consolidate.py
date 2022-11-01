# 赛亚人
class Saiyan:
    hair = '黑发'

    # 每个赛亚人战斗力不同
    def __init__(self, ATK):
        self.ATK = ATK


# 请在下方定义“超级赛亚人”类
class SuperSaiyan(Saiyan):
    # 超级赛亚人能够变身
    def transform(self):
        # 变身后发色变为金色
        self.hair = '金色'
        # 战斗力变为原来的 50 倍
        self.ATK *= 50


# 卡卡罗特是超级赛亚人，初始战斗力为 25
kakarot = SuperSaiyan(25)
# 他是赛亚人
if isinstance(kakarot, Saiyan):
    print('卡卡罗特是赛亚人，长着一头{}'.format(kakarot.hair))
else:
    print('卡卡罗特不是赛亚人')
print('他的战斗力是 {}'.format(kakarot.ATK))

# 并且能通过变身提升战斗力
print('卡卡罗特伴随着一阵金光，开始变身！')
kakarot.transform()
print(f'变身后的战斗力是 {kakarot.ATK}，头发也变成了{kakarot.hair}')
