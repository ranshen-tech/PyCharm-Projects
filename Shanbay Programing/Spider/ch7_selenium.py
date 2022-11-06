"""
有一个 class="more-link" 的 a 元素。请你用刚刚学到的方法找到该元素，并把它的 href 属性的值打印出来吧。
"""
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
url = 'https://wpblog.x0y1.com'
browser.get(url)
a = browser.find_element('class name', 'more-link')
print(a.get_attribute('href'))
soup = BeautifulSoup(browser.page_source, 'html.parser')
result = soup.select_one('a.more-link')
print(result['href'])
print(result.attrs['href'])
browser.close()
# browser.quit()
