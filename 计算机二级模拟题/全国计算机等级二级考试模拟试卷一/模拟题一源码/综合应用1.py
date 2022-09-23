# fi = open('论语-网络版.txt', 'r', encoding='utf-8')
# fo = open('论语-提取版.txt', 'w', encoding='utf-8')
# wflag = False
# for item in fi:
#     if '【' in item:
#         wflag = False
#     if '【原文】' in item:
#         wflag = True
#         continue
#     if wflag == True:
#         for i in range(0, 25):
#             for j in range(0, 45):
#                 item = item.replace('{}·{}'.format(i, j), '')
#         fo.write(item)
#
# fi.close()
# fo.close()


# f = open('论语-网络版.txt')
# fw = open('论语读取版.txt', 'w')
# flag = None
# for line in f:
#     if '【' in line:
#         flag = False
#     if '【原文】' in line:
#         flag = True
#         continue
#     if flag:
#         line = line.strip(' 1234567890·')
#         fw.write(line)
# f.close()
# fw.close()

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
                for i in range(1, 31):
                    line = line.replace(f'({i})', '')
                fw.write(line)
