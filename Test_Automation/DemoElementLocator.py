from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.find_element(by=By.NAME, value='user-name').send_keys('standard_user')
        driver.find_element(by=By.NAME, value='password').send_keys('secret_sauce')
        driver.find_element(by=By.NAME, value='login-button').click()

        wait = WebDriverWait(driver, 10)
        driver.find_element(by=By.XPATH, value='//*[@id="react-burger-menu-btn"]').click()

        # Use a different locating strategy to find the "About" link
        about_link = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'About')))
        about_link.click()

FindbyID = DemoFindElementByIDandName()
FindbyID.locate_by_id_demo()
