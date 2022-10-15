__author__ = 'ranshen0519@icloud.com'
from urllib.request import urlopen
import ssl

url = urlopen("https://www.runoob.com/", context=ssl._create_unverified_context())
print(url)
