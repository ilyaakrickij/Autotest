from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def sum(num1atr, num2atr):
    return str(num1atr + num2atr)

            


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1atr = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    num2atr = int(num2.text)
    y= sum(num1atr, num2atr)
    seeelct = Select(browser.find_element_by_tag_name ("select"))
    seeelct.select_by_value(y)

    
    
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"
    # robotrule = browser.find_element_by_id("robotsRule")
    # robots_checked = robotrule.get_attribute("checked")
    # print(robots_checked)
    # assert robots_checked is None
    # Ваш код, который заполняет обязательные поля
    # x_element = browser.find_element_by_id("input_value")
    # x = atributeklad
    # y = calc(x)
    
    # robot = browser.find_element_by_id("robotCheckbox").click()
    # robotrule = browser.find_element_by_id("robotsRule")
    # robotrule.click()
    submit = browser.find_element_by_css_selector("button.btn").click()

    # firstname = browser.find_element_by_css_selector(".first_block .form-group.first_class .form-control.first")
    # firstname.send_keys("Smolensk")
    # lastname = browser.find_element_by_css_selector(".first_block .form-group.second_class .form-control.second")
    # lastname.send_keys("Smolensk")
    # email = browser.find_element_by_css_selector(".first_block .form-group.third_class .form-control.third")
    # email.send_keys("Smolensk")

    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
