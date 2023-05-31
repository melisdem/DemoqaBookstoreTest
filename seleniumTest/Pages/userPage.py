from selenium.webdriver.common.by import By
from seleniumTest.Locators.locators import Locators

class UserPage():
    def __init__(self, driver):
        self.driver = driver

        # defining objects by id
        self.book_link_text = Locators.book_link_text

    def click_book(self):
        self.driver.find_element(By.LINK_TEXT, self.book_link_text).click()