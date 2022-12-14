"""
turtle库使用
"""
import time
import turtle as t
# t.penup()
# t.goto(-200, -50)
# t.pendown()
# t.begin_fill()
# t.color('red')
# t.circle(40, steps=3)  # 三角形
# t.end_fill()

# t.penup()
# t.goto(-100, -50)
# t.pendown()
# t.begin_fill()
# t.color('blue')
# t.circle(40, steps=4)  # 四边形
# t.end_fill()

# t.penup()
# t.goto(0, -50)
# t.pendown()
# t.begin_fill()
# t.color('green')
# t.circle(40, steps=5)  # 五边形
# t.end_fill()

# t.penup()
# t.goto(100, -50)
# t.pendown()
# t.begin_fill()
# t.color('yellow')
# t.circle(40, steps=6)
# t.end_fill()

# t.penup()
# t.goto(200, -50)
# t.pendown()
# t.begin_fill()
# t.color('purple')
# t.circle(40)  # 圆
# t.end_fill()
# t.hideturtle()  # 把笔隐藏

# time.sleep(1)


# 绘制边长200的正方形
# d = 0
# for i in range(4):
#     t.fd(200)
#     d += 90
#     t.seth(d)


# def draw_circle(n):
#     t.penup()
#     t.goto(0, -n)
#     t.pendown()
#     t.circle(n)


# for i in range(20, 80, 20):
#     draw_circle(i)
# t.done()


# for i in range(6):
#     t.fd(100)
#     t.left(60)
# t.done()


"""
random库使用
"""
import random
# random.seed(10)  # 种子默认是系统时间
# print(random.random())
# print(random.random())
# random.seed(10)  # 种子相同，产生的随机数也相同
# print(random.random())
# print(random.random())

# ran = random.randrange(1, 4, 2)  # [start, stop, step)
# print(ran)

# ran = random.uniform(1, 2)  # 生成一个[a, b]随机数
# print(ran)

# print(random.choice('python'))

# lst = [1, 2, 3]
# random.shuffle(lst)  # 打乱列表lst位置，并返回None
# print(lst)
# print(random.sample(lst, 2))  # 选择样本，抽奖


"""
time库使用
"""
# print(time.ctime(time.time()))
# print(time.ctime())
