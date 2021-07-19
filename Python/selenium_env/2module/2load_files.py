import os 
from selenium import webdriver
import math

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Aid@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "kek.txt"
    file_path = os.path.join(current_dir, 'kek.txt')
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()



# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path)