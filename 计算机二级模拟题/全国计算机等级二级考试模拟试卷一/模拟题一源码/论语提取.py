with open('论语-网络版.txt') as f:
    with open('论语提取版-原文.txt', 'w') as fw:
        flag = None
        for line in f:
            if '【' in line:
                flag = False
            if '【原文】' in line:
                flag = True
                continue
            if flag:
                line = line.strip(' 1234567890·')
                for i in range(50):
                    line = line.replace(f'({i})', '')
                fw.write(line)
