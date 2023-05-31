from selenium.webdriver.common.by import By
from seleniumTest.Locators.locators import Locators

class HomePage():
    def __init__(self,driver):
        self.driver = driver

        # defining objects by id
        self.login_button_id = Locators.login_button_id

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()