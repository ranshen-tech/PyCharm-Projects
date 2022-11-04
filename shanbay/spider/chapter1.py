# '#'后面的部分叫做 锚点，也是 URL 成分之一，用于快速定位到页面对应内容
# 可搜索 域名解析 了解更多。
"""
'https://wpblog.x0y1.com/?p=211'

"""
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 新建 Excel 工作簿，设置工作表
wb = Workbook()
ws = wb.worksheets[0]
ws.title = '数据'

# 访问网页
res = requests.get('https://wpblog.x0y1.com/?p=211')
# 判断网页是否访问成功
if res.status_code == 200:
    print('访问成功，开始解析网页')
    # 解析网页
    soup = BeautifulSoup(res.text, 'html.parser')
    # 提取网页表格数据写入工作表
    table = soup.select('table.has-fixed-layout > tbody tr')
    for row in table:
        row_list = [column.text for column in row.select('td')]
        ws.append(row_list)
    print('解析并提取完毕')
else:
    print('访问失败，状态码：{}'.format(res.status_code))

# 保存 Excel 文件
wb.save('电商转化流程.xlsx')

print('\n手机端无法下载 Excel 文件，下面是 Excel 的预览')
import pandas as pd

df = pd.read_excel('电商转化流程.xlsx')
print(df)
