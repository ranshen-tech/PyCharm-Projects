__author__ = 'ranshen0519@icloud.com'
import requests
from bs4 import BeautifulSoup
import time
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# 登陆参数
login_data = {
    'log': 'codetime',
    'pwd': 'shanbey520',
    'wp-submit': '登录',
    'redirect_to': 'https://wpblog.x0y1.com',
    'testcookie': '1'
}
# 创建一个session类对象,可以像requests对象一样使用get post方法
session = requests.Session()
# 设置session的全局headers
session.headers.update(headers)  # 默认使用全局headers
# 获得登陆请求对象
login_res = session.get('https://wpblog.x0y1.com/wp-login.php', data=login_data)
# 获得python分类文章
comment_res = session.get('https://wpblog.x0y1.com/?cat=2')
# 解析静态页面
soup = BeautifulSoup(comment_res.text, 'html.parser')
# 获取所有代表标题的a标签内容
titles = soup.select('h2.entry-title a')
# 获取所有文章链接
links = [title['href'] for title in titles]

for link in links:
    # 获取文章页面内容
    res_psg = session.get(link)
    # 解析文章
    soup_psg = BeautifulSoup(res_psg.text, 'html.parser')
    # 通过标签获取文章内容
    content = soup_psg.select('div.entry-content')[0]
    # 打印文章内容，去掉前后空格
    print(content.text.strip())
    # break
    time.sleep(0.5)  # ❗️注意控制频率

