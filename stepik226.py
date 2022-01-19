from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
vvod = browser.find_element_by_xpath("//input[@id='answer']")
browser.execute_script("return arguments[0].scrollIntoView(true);", vvod)
vvod.send_keys(y)
irobot = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
robotsrule = browser.find_element_by_xpath("//input[@id='robotsRule']").click()
submit = browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()




time.sleep(7)
browser.quit()