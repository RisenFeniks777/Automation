from selenium import webdriver
import time


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(r"C:\Users\Firripu\Desktop\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        driver.find_element_by_xpath("//input[@id='user-name']").send_keys('standar_user')
        driver.find_element_by_xpath("//input[@id='password']").send_keys('secreat_sauce')
        driver.find_element_by_id('login-button').click()


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()