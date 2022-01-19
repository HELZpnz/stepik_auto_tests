from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    sunduk = browser.find_element_by_xpath("//img[@id='treasure']")
    x = sunduk.get_attribute("valuex")
    y = calc(x)
    rezultat = browser.find_element_by_xpath("//input[@id='answer']")
    rezultat.send_keys(y)
    nerobot = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    nerobot.click()
    robots_rule = browser.find_element_by_xpath("//input[@id='robotsRule']")
    robots_rule.click()
    submit = browser.find_element_by_xpath("//button[contains(text(),'Submit')]")
    submit.click()
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"

    #assert robots_checked is None


    print(x)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()