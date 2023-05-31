from selenium.webdriver.common.by import By
from seleniumTest.Pages.userPage import UserPage
from seleniumTest.Locators.locators import Locators

class ProfilePage():
    def __init__(self, driver):
        self.driver = driver

        # defining objects
        self.parentDiv_class_name = Locators.parentDiv_class_name
        self.childDiv_class_selector = Locators.childDiv_class_selector
        self.logout_xpath = Locators.logout_xpath
        self.deleteBook_id = Locators.deleteBook_id

    # in cart there can be other books so I want to loop over list and select the right one
    # however in chrome driver i can not select the the right element in the below code block
    # self.driver.find_element(By.CLASS_NAME, self.parentDiv_class_name).find_elements(By.CSS_SELECTOR, self.childDiv_class_selector)
    # so I can use simply
    # assert userPage.book_link_text in driver.page_source
    # instead of looping but also in the profile page book can be placed somewhere else other than cart(like an advertise)
    # so i choose looping

    def loopOverCart(self, bool):
        driver = self.driver
        userPage = UserPage(driver)
        myParentDiv = self.driver.find_element(By.CLASS_NAME, self.parentDiv_class_name)
        myDiv = myParentDiv.find_elements(By.CSS_SELECTOR, self.childDiv_class_selector)
        result = False
        for elm in myDiv:
            print(elm.text, result)
            if elm.text == userPage.book_link_text:
                result = bool
            else:
                pass
        return result

    def checkCart(self):
        assert self.loopOverCart(True) == True


    def userLogout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def removeBook(self):
        driver = self.driver
        driver.find_elements(By.ID, self.deleteBook_id)[-1].click()


    def checkCartRemoveBook(self):
        assert self.loopOverCart(True) == False
