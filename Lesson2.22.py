from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os



            

try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/file_input.html "
    browser.get(link)
    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # x_elemeu = browser.find_element_by_id("input_value")
    # x = x_elemeu.text
    # y = calc(x)
    # inpuut = browser.find_element_by_id("answer")
    # inpuut.send_keys(y)
    # time.sleep(2)
    # robot = browser.find_element_by_id("robotCheckbox").click()
    # roborbut = browser.find_element_by_id("robotsRule")
    # roborbut.click()
    # submit = browser.find_element_by_css_selector("button.btn").click()
    

    name = browser.find_element_by_name('firstname')
    name.send_keys("ilya")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("pupkin")
    email = browser.find_element_by_name("email")
    email.send_keys("mail@mail.ru")
    fileee = browser.find_element_by_id("file")
    dirr = os.path.abspath(os.path.dirname(__file__))
    fileepa = os.path.join(dirr, 'test.txt')
    fileee.send_keys(fileepa)
    submiit = browser.find_element_by_css_selector("button.btn").click()



    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
