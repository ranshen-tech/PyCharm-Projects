__author__ = 'ranshen0519@icloud.com'
from selenium import webdriver
import time

browser = webdriver.Chrome()
# 打开博客
browser.get('https://wpblog.x0y1.com')
# 找到登陆按钮
login_btn = browser.find_element('link text', '登陆')
# 点击登陆按钮
login_btn.click()
# 等待2秒钟，等页面加载完毕
time.sleep(2)
# 找到用户名输入框
user_login = browser.find_element('id', 'user_login')
# 输入用户名
user_login.send_keys('codetime')
# 找到密码输入框
user_pass = browser.find_element('id', 'user_pass')
# 输入密码
user_pass.send_keys('shanbay520')
# 找到登陆按钮
wp_summit = browser.find_element('id', 'wp_submit')
# 点击登陆按钮
wp_summit.click()
# 找到python分类文章链接
# python_cat = browser.find_element('link text', 'python')
python_cat = browser.find_element('css selector', 'section#categories-2 ul li a')
# 点击该分类
python_cat.click()
# 找到跳转的页面中的所有文章标题元素
titles = browser.find_elements('css selector', 'h2.entry-title a')
# 找到标题元素中的内含链接
links = [title.get_attribute('href') for title in titles]
# 依次打开links中的链接

