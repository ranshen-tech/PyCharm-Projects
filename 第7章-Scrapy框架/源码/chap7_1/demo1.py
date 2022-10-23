#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  requests
resp=requests.get('https://book.douban.com/top250')
print(resp.text)