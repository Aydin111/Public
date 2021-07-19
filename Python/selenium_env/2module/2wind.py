from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	alert = browser.switch_to.alert
	alert.accept()
	time.sleep(2)
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_css_selector("input#answer")
	input1.send_keys(calc(x))

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()