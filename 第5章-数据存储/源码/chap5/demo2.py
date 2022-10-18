#教育机构 ：马士兵教育
#讲    师：杨淑娟
#课堂案例
import  requests
import json
def send_request():
    url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=7252335&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    return resp.text

def parse_json(data):
    return data.replace('fetchJSON_comment98(','').replace(');','')   #如果为str类型


def type_change(data):
    return json.loads(data)

def save(obj):
    json.dump(obj,open('京东销售最好的粽子数据.txt','w',encoding='utf-8'),ensure_ascii=False)
def start():
    data=send_request()
    obj=parse_json(data)
    #print(type(type_change(s)))
    save(obj)
    #print(s)


if __name__ == '__main__':
    start()


