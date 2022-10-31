__author__ = 'ranshen0519@icloud.com'
import hmac
import hashlib

# new（key,msg=None,digestmod）方法
# 创建哈希对象
# key和digestmod参数必须指定，key和msg（需要加密的内容）均为bytes类型，digestmod指定加密算法，比如‘md5’,'sha1'等
# 对象digest（）方法：返回bytes类型哈希值

# 对象hexdigest（）方法：返回十六进制哈希值
key = "key".encode()
text = "msb".encode()
m = hmac.new(key, text, hashlib.sha256)
print(m.digest())
print(m.hexdigest())
