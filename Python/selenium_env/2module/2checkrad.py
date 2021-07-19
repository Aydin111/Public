from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
import time

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(calc(x))
    button = browser.find_element_by_css_selector('[type="checkbox"]')
    button.click()
    
    button = browser.find_element_by_css_selector('[value="robots"]')
    button.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
