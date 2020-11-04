from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):  
    # return str(math.lоg(abs(12*math.sin(int(x)))))
    return str(math.log(abs(12*math.sin(int(x)))))


            

try:
    browser = webdriver.Chrome()
    link = " https://SunInJuly.github.io/execute_script.html "
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    x_elemeu = browser.find_element_by_id("input_value")
    x = x_elemeu.text
    y = calc(x)
    inpuut = browser.find_element_by_id("answer")
    inpuut.send_keys(y)
    time.sleep(2)
    robot = browser.find_element_by_id("robotCheckbox").click()
    roborbut = browser.find_element_by_id("robotsRule")
    roborbut.click()
    submit = browser.find_element_by_css_selector("button.btn").click()
    

    assert True
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
