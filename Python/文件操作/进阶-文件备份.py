"""
1.读取文件
2.将文件写入 'bill.txt.bak' 文件操作
3.将文件内标记为'测试'的数据行丢弃
"""
fr = open('/Python/文件操作/bill.txt', 'r', encoding='UTF-8')
fw = open('/Python/文件操作/bill.txt.bak', 'w', encoding='UTF-8')
for line in fr:
    if line.strip().split(',')[4] == '正式':
        fw.write(line)
fr.close()
fw.close()

