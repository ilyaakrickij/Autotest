from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    # return str(math.log(abs(12*math.sin(int(x)))))




            

try:
    
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/redirect_accept.html "
    browser.get(link)
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()
    new_window = browser.window_handles[1]
    new_str = browser.switch_to_window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    inpuut = browser.find_element_by_id("answer")
    inpuut.send_keys(y)
    suubbmit = browser.find_element_by_css_selector("button.btn").click()
   

    


    

    



    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
