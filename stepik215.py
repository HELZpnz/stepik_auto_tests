from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    otvet=browser.find_element_by_xpath("//input[@id='answer']")
    otvet.send_keys(y)
    nerobot=browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    nerobot.click()
    robots_rule=browser.find_element_by_xpath("//input[@id='robotsRule']")
    robots_rule.click()
    submit=browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    submit.click()







finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()