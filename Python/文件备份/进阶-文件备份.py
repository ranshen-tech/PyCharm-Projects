"""
1.读取文件
2.将文件写入 'bill.txt.bak' 文件备份
3.将文件内标记为'测试'的数据行丢弃
"""
fr = open('/Users/ranshen/PyCharm Projects/Python/文件备份/bill.txt', 'r', encoding='UTF-8')
fw = open('/Users/ranshen/PyCharm Projects/Python/文件备份/bill.txt.bak', 'w', encoding='UTF-8')
for line in fr:
    if line.strip().split(',')[4] == '正式':
        fw.write(line)
fr.close()
fw.close()

