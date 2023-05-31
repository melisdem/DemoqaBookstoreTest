from selenium.webdriver.common.by import By
from seleniumTest.Locators.locators import Locators

class BookPage():
    def __init__(self, driver):
        self.driver = driver

        # defining objects
        self.add_button_css = Locators.add_button_css

    def add_book(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_button_css).click()