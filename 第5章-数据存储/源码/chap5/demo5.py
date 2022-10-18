#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  requests
import  json
import  csv
def send_request():
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=7252335&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    return resp.text



def parse_html(data):
    s=data.replace('fetchJSON_comment98(', '').replace(');', '')
    dict_data=json.loads(s)
    comments_list=dict_data['comments']
    lst=[]
    for comment in comments_list:
        content=comment['content'] #评论的内容
        creationTime=comment['creationTime'].split(' ')[0]  #获取评论时间
        lst.append([content,creationTime])
    save(lst)
def save(lst):
    with open('粽子的评论数据.csv','w',newline='')as file:
        writer=csv.writer(file)
        writer.writerows(lst)

def start():
    data=send_request()
    parse_html(data)

if __name__ == '__main__':
    start()