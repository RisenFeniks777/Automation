from selenium import webdriver
import time


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(r"C:\Users\Firripu\Desktop\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        driver.find_element_by_id('user-name').send_keys('standard_user')
        driver.find_element_by_id('password').send_keys('secret_sauce')
        time.sleep(5)


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()