"""
官方文档基础教程：
https://docs.python.org/zh-cn/3.11/howto/logging.html#logging-basic-tutorial
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    # datefmt='%a %d %b %Y %H:%M:%S',
                    datefmt='%Y %m %d %H:%M',
                    # filename='my.log',
                    # filemode='w'
                    )

# logging.basicConfig(
                    # filename=path + 'log_' + today_date + '.txt',
                    # level=logging.DEBUG, filemode='a',
                    # format='%(asctime)s %(levelname)s >>>  %(message)s',
                    # datefmt='%Y-%m-%d %H:%M')

url = 'www.baidu.com'
logging.info('scraping %s...', url)
# logging.info('This is a info.')
# logging.debug('This is a debug message.')
# logging.warning('This is a warning.')
# 输出到同目录下 my.log 文件中的内容：
# Wed 05 Jun 2019 22:25:32 test.py INFO This is a info.
# Wed 05 Jun 2019 22:25:32 test.py WARNING This is a warning.
