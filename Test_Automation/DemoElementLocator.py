from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.find_element(by=By.NAME, value='user-name').send_keys('standard_user')
        driver.find_element(by=By.NAME, value='password').send_keys('secret_sauce')
        driver.find_element(by=By.NAME, value='login-button').click()
        time.sleep(5)


FindbyID = DemoFindElementByIDandName()
FindbyID.locate_by_id_demo()
