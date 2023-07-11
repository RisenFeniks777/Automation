from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

print(driver.title)
time.sleep(5)
driver.close()  # Use quit() instead of close() to completely terminate the WebDriver instance
