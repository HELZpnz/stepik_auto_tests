from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
okno1 = browser.find_element_by_xpath("//button[contains(text(),'I want to go on a magical journey!')]").click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
vvod = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
submit = browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()



time.sleep(7)
browser.quit()


