from selenium import webdriver
import time
import os#модуль для загрузки файлов


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
first_name = browser.find_element_by_css_selector("body.bg-light:nth-child(2) div.container:nth-child(2) form:nth-child(2) div.form-group:nth-child(1) > input.form-control:nth-child(2)")
first_name.send_keys("Yury")
last_name = browser.find_element_by_css_selector("body.bg-light:nth-child(2) div.container:nth-child(2) form:nth-child(2) div.form-group:nth-child(1) > input.form-control:nth-child(4)")
last_name.send_keys("Zhevakin")
pochta = browser.find_element_by_css_selector("body.bg-light:nth-child(2) div.container:nth-child(2) form:nth-child(2) div.form-group:nth-child(1) > input.form-control:nth-child(6)")
pochta.send_keys('xelz@bk.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))#указываем деррикториию, лежит вместе с файлом теста
file_name = "file_example.txt"# указываем название файла
file_path = os.path.join(current_dir, file_name)#все применяем
zagruzka = browser.find_element_by_xpath("//input[@id='file']")
zagruzka.send_keys(file_path)
submit = browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()



time.sleep(7)
browser.quit()