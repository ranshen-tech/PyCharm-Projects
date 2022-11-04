__author__ = 'ranshen0519@icloud.com'

import time
from selenium import webdriver

browser = webdriver.Chrome()
# 打开博客
browser.get('https://wpblog.x0y1.com')
# 找到登陆按钮
login_btn = browser.find_element('link text', '登录')
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
# 找到登录按钮
wp_summit = browser.find_element('id', 'wp-submit')
# 点击登陆按钮
wp_summit.click()
# 找到python分类文章链接
python_cat = browser.find_element('css selector', 'section#categories-2 ul li a')
# 点击该分类
python_cat.click()
# 找到跳转的页面中的所有文章标题元素
titles = browser.find_elements('css selector', 'h2.entry-title a')
# 找到标题元素中的内含链接
links = [title.get_attribute('href') for title in titles]
# 依次打开links中的链接
for link in links:
    browser.get(link)
    # 获取文章正文内容
    content = browser.find_element('class name', 'entry-content')
    print(content.text)

browser.quit()


# 为了提升爬取效率，我们可以将浏览器设置为静默模式，让浏览器不必真的打开，而是在后台默默地获取数据、操作页面。
# from selenium import webdriver

# 初始化配置
# options = webdriver.ChromeOptions()
# headless 为静默模式
# options.add_argument('--headless')
# 将配置传入浏览器
# browser = webdriver.Chrome(options=options)
# 打开网页
# browser.get('https://wpblog.x0y1.com')
# 关闭浏览器
# browser.quit()
