from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    # return str(math.log(abs(12*math.sin(int(x)))))




            

try:
    
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/explicit_wait2.html "
    browser.get(link)
    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    




    # browser.get(link)
    submit = browser.find_element_by_id("book")
    submit.click()

    # new_window = browser.window_handles[1]
    # new_str = browser.switch_to_window(new_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    inpuut = browser.find_element_by_id("answer")
    inpuut.send_keys(y)
    suubbmit = browser.find_element_by_id("solve").click()
   

    


    

    



    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
