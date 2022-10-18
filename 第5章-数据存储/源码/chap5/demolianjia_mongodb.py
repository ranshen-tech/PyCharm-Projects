#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  requests
from bs4 import  BeautifulSoup
import pymongo

class LianJiaSpider():


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
            lst.append({'title':title,
                        'houseinfo':houseInfo,
                        'positioninfo':positionInfo,
                        'dealDate':dealDate,
                        'number':number,
                        'unitPrice':unitPrice,
                        'dealHouseTxt':dealHouseTxt,
                        'deal_money':span_list[0].text,
                        'deal_date':span_list[1].text,
                        'agent_anme':agent_name})
        #print(lst)
        self.save(lst)  #调用存储数据的方法
    def save(self,lst):
        #获取连接对象
        client=pymongo.MongoClient('localhost',27017)

        #获取要操作的数据库
        db=client['lianjia']

        #获取collection
        collection=db['collection_lianjia']

        collection.insert_many(lst)


    def start(self):
        for i in range(1,2):
            full_url=self.url.format(i)
            resp=self.send_request(full_url)
            #print(resp.text)
            self.parse_html(resp)

if __name__ == '__main__':
    lianjia=LianJiaSpider()
    lianjia.start()


