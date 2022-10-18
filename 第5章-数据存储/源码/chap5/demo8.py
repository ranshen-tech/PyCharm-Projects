#教育机构 ：马士兵教育
#讲    师：杨淑娟
#课堂案例-爬取下厨房的菜品数据
import  requests
from  bs4 import  BeautifulSoup
import  openpyxl

def send_request():
    url='http://www.xiachufang.com/explore/'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    return resp.text

def parse_html(html):
    #解析数据
    count=0
    bs=BeautifulSoup(html,'lxml')
    lst_name=bs.find_all('p',class_='name')
    lst_category=bs.find_all('p',class_='ing ellipsis')
    #print(lst_name)
    #print(lst_category)
    lst=[]
    for i in range(len(lst_name)):
        count+=1
        food_url='http://www.xiachufang.com/'+lst_name[i].find('a')['href']
        #print(food_url)
        lst.append([count,lst_name[i].text[18:-14],lst_category[i].text[1:-1],food_url])
    #print(lst)
    save(lst)
def save(lst):
    wb=openpyxl.Workbook()
    sheet=wb.active
    for row in lst:
        sheet.append(row)
    wb.save('下厨房美食.xlsx')

def start():
    result=send_request()
    parse_html(result)

if __name__ == '__main__':
    start()

