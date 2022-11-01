__author__ = 'ranshen0519@icloud.com'


# 萨摩耶犬
class Samoyed: pass


# 柯基犬
class Corgi: pass


# 牧羊犬
class Collie: pass


def welcome(animal):
    # 需要逐个判断 animal 是不是已知犬种
    if type(animal) in [Samoyed, Corgi, Collie]:
        print('经检测，这是一只小狗，欢迎进入狗狗乐园！')
    else:
        print('这好像不是狗狗，不好意思，不能进入狗狗乐园')


dingding = Samoyed()
welcome(dingding)
# 输出：经检测，这是一只小狗，欢迎进入狗狗乐园！
