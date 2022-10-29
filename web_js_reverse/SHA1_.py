__author__ = 'ranshen0519@icloud.com'

import hashlib

sha1 = hashlib.sha1()
data = "msb"
sha1.update(data.encode("utf-8"))
sha1_data = sha1.hexdigest()
print(sha1_data)


# 解密工具：http://tool.geekapp.cn/index.php
# https://www.5axxw.com/tools/web/encrypt/encrypt2.html
