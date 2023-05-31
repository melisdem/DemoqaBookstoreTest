import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# importing pages since we are using POM
from seleniumTest.Pages.loginPage import LoginPage
from seleniumTest.Pages.homePage import HomePage
from seleniumTest.Pages.userPage import UserPage
from seleniumTest.Pages.bookPage import BookPage
from seleniumTest.Pages.profilePage import ProfilePage

class TestLoginAddBook():
  def setup_method(self, method):
    # it does not work with chrome driver. I explain in the profilePage
    # self.driver = webdriver.Chrome(executable_path="seleniumTest/drivers/chromedriver")
    self.driver = webdriver.Firefox()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_01_loginAddBook(self):
    driver = self.driver
    driver.get("https://demoqa.com/books")
    driver.maximize_window()

    home = HomePage(driver)
    home.click_login()

    print("Logging in")
    login = LoginPage(driver)
    login.enter_username("MelDem")
    login.enter_password("Mel123,@Dem")
    login.click_login()


    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

    print("Logged in and can see the books")
    userPage = UserPage(driver)
    userPage.click_book()

    print("clicked the book")
    bookPage = BookPage(driver)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    bookPage.add_book()
    time.sleep(2)

    print("book added, going to cart")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("accepted")
    driver.find_element(By.CSS_SELECTOR, ".show #item-3").click()
    print("nav bar clicked")

    print("in the cart, checking book added or not")
    profilePage = ProfilePage(driver)
    profilePage.checkCart()

    time.sleep(3)

    print("logging out")
    profilePage.userLogout()


  def test_02_addAndremoveBook(self):
    driver = self.driver
    driver.get("https://demoqa.com/books")
    driver.maximize_window()

    print("Bookstore page click login")
    home = HomePage(driver)
    home.click_login()

    print("Logging in")
    login = LoginPage(driver)
    login.enter_username("MelDem")
    login.enter_password("Mel123,@Dem")
    login.click_login()

    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

    print("Logged in and can see the books")
    userPage = UserPage(driver)
    userPage.click_book()

    print("clicked the book")
    bookPage = BookPage(driver)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    bookPage.add_book()
    time.sleep(2)

    print("book added, going to cart")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("accepted")
    driver.find_element(By.CSS_SELECTOR, ".show #item-3").click()
    print("nav bar clicked")

    print("in the cart, removing book")
    profilePage = ProfilePage(driver)
    profilePage.removeBook()
    time.sleep(1)
    self.driver.find_element(By.ID, "closeSmallModal-ok").click()
    print("confirm delete")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    print("check remove")
    time.sleep(2)
    profilePage.checkCartRemoveBook()

    time.sleep(3)

    print("logging out")
    profilePage.userLogout()


