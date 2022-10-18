#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  csv
with open('student.csv','a+',newline='') as file:
    #创建一个writer对象
    writer=csv.writer(file)
    #一次写一行数据
    writer.writerow(['麻七',23,90])
   #一次写入多行数据
    lst=[
        ['Jack',23,98],
        ['Marry',22,87],
        ['Lili',22,76]
    ]
    writer.writerows(lst)
