from selenium.webdriver.common.by import By
from seleniumTest.Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        # we can now use driver instead of self.driver everytime
        self.driver = driver

        # defining objects by id
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id

    def enter_username(self, username):
        # if there is text in the username textbox clear
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        # if there is text in the password textbox clear
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()