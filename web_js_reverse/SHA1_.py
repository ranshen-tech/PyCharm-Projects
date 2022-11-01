__author__ = 'ranshen0519@icloud.com'

import hashlib

hash_ = hashlib.sha1()
hash_.update('ranshen'.encode("utf-8"))
print(hash_.hexdigest())
print(hash_.digest())


# 解密工具：http://tool.geekapp.cn/index.php
# https://www.5axxw.com/tools/web/encrypt/encrypt2.html
