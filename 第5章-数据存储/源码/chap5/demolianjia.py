#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  requests
from bs4 import  BeautifulSoup
import  mysql.connector

class LianJiaSpider():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test',auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    def __init__(self):
        self.url='https://bj.lianjia.com/chengjiao/pg{0}/'
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}

    def send_request(self,url):
        resp=requests.get(url,headers=self.headers)
        if resp.status_code==200:
            return resp

    def parse_html(self,resp):
        lst=[]
        html=resp.text
        bs=BeautifulSoup(html,'lxml')
        ul=bs.find('ul',class_='listContent')
        li_list=ul.find_all('li')
        for item in li_list:
            title=item.find('div',class_='title').text
            houseInfo=item.find('div',class_="houseInfo").text
            positionInfo=item.find('div',class_='positionInfo').text
            dealDate= item.find('div',class_='dealDate').text
            number=item.find('span',class_='number').text+'万'
            unitPrice=item.find('div',class_='unitPrice').text
            dealHouseTxt=item.find('span',class_='dealHouseTxt')
            if dealHouseTxt!=None:
                dealHouseTxt=dealHouseTxt.text
            else:
                dealHouseTxt=''
            span=item.find('span',class_='dealCycleTxt')
            span_list=span.find_all('span')
            agent_name=item.find('a',class_='agent_name').text

            #print(agent_name)
            lst.append((title,houseInfo,positionInfo,dealDate,number,unitPrice,dealHouseTxt,span_list[0].text,span_list[1].text,agent_name))
        #print(lst)
        self.save(lst)  #调用存储数据的方法
    def save(self,lst):
        sql='insert into tb_lianjia (title,houseInfo,positionInfo,dealDate,totalPrice,unitPrice,dealHouseTxt,deal_money,deal_date,agent_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.mycursor.executemany(sql,lst)
        self.mydb.commit()
        print(self.mycursor.rowcount,'插入完毕')


    def start(self):
        for i in range(1,2):
            full_url=self.url.format(i)
            resp=self.send_request(full_url)
            #print(resp.text)
            self.parse_html(resp)

if __name__ == '__main__':
    lianjia=LianJiaSpider()
    lianjia.start()


