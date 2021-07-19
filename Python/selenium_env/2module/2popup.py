from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return int(x1+y1)
try: 
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_css_selector("h2 span:nth-child(2)")
	x = x_element.text
	x1 = int(x)
	y_element = browser.find_element_by_css_selector("h2 span:nth-child(4)")
	y = y_element.text
	y1 = int(y)
	z = calc(x)
	select = Select(browser.find_element_by_tag_name("select"))# просто жмем на выпадающий список
	select.select_by_value(str(calc(x))) # ищем элемент с текстом (результат вычисления)
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()