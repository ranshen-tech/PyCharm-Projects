__author__ = 'ranshen0519@icloud.com'

import hashlib

pwd = "123"
# 生成MD5对象
m = hashlib.md5()
# 对数据进行加密
m.update(pwd.encode('utf-8'))
print(m)
# 获取密文
pwd = m.hexdigest()
print(pwd)


# 解密工具：https://www.cmd5.com/
