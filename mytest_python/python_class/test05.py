from selenium import webdriver
import time
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://erp.lemfix.com")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
time.sleep(5)
driver.quit()