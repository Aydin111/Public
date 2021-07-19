from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
import time
import math
	
try: 
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	button = WebDriverWait(browser, 14).until(
    	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
	button = browser.find_element_by_css_selector("button#book")
	button.click()

	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element_by_css_selector("input#answer")
	input1.send_keys(calc(x))

	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	browser.implicitly_wait(1)
	button = browser.find_element_by_css_selector("#solve")
	button.click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()