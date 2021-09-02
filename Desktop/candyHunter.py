from selenium import webdriver
import time

url = "https://coingecko.com/"
driver = webdriver.Firefox(executable_path=r'PATH_TO_geckodriver\geckodriver.exe') 
driver.get(url)

loginButton = driver.find_element_by_class_name('mr-3.text-black').click()

driver.find_element_by_name("user[email]").send_keys("ENTER_email")

driver.find_element_by_name("user[password]").send_keys("ENTER_password")

driver.find_element_by_class_name("btn.btn-primary.btn-lg.btn-block").click()

driver.find_element_by_class_name("candy-notification-icon").click()

driver.find_element_by_class_name("btn.btn-primary.col-12.collect-candy-button").click()

driver.quit()
