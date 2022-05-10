

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
driver.quit()

