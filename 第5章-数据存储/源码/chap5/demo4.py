#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  csv
with open('student.csv','r',newline='') as file:
    #创建reader对象
    reader=csv.reader(file)
    for row in reader:
        print(row)

