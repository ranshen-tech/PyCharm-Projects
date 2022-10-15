# urllib.parse  用于解析url
import urllib.parse
kw = {'wd': '马士兵'}
# 编码
result = urllib.parse.urlencode(kw)
print(result)
# https://www.baidu.com/s?wd=%E9%A9%AC%E5%A3%AB%E5%85%B5&rsv_spt=1&rsv_iqid=0xcff86fcd0005ded5&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=9&rsv_sug1=7&rsv_sug7=100

# 解码
response = urllib.parse.unquote(result)
print(type(response))
print(response)
