from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
a = browser.find_element_by_css_selector('#num1').text
b = browser.find_element_by_css_selector('#num2').text
summ = str(int(a)+int(b))
vibor = browser.find_element_by_xpath("//select[@id='dropdown']").click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(summ)

submit = browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
time.sleep(7)
    # закрываем браузер после всех манипуляций
browser.quit()