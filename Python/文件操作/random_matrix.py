"""
生成一个10*10的随机矩阵并保存文件，空格分隔行向量，换行分隔列向量。
再写程序将刚才保存的矩阵文件另存为CSV格式，用文本编辑器打开看看
"""
import random
with open('random_matrix.txt', 'w') as f:
    for line in range(10):
        word = ''
        for row in range(10):
            word += f'{str(random.randint(1, 100))}\t'
        f.write(f'{word}\n')


with open('random_matrix.txt') as txt:
    with open('random_matrix.csv', 'w') as csv:
        for line in txt:
            s = line.replace(' ', ',')  # csv文件以逗号分隔
            csv.write(s)
