from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
knopka = browser.find_element_by_xpath("//button[contains(text(),'I want to go on a magical journey!')]").click()


new_window = browser.window_handles[1]# даем назвачение новой вкладки
browser.switch_to.window(new_window)# делаем переход на нужную нам вкладку, в скобках значение вкладки
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
vvod = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
submit = browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()



time.sleep(7)
browser.quit()
