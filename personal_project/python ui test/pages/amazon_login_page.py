from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePageLocators
from utils.CustomLogger import CustomLogger
import time
logger = CustomLogger()


class AmazonLoginPageLocators(BasePageLocators):
    INPUT_EMAIL = (By.ID, "ap_email")
    INPUT_PASSWORD = (By.ID, "ap_password")
    BTN_CONTINUE = (By.CSS_SELECTOR, "span#continue")
    BTN_LOGIN = (By.CSS_SELECTOR, "span[id='auth-signin-button']")


class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_with_given_user_and_pass(self, username, password):
        logger.info("Login With Given User And Pass: ", username, password)
        self.fill_username(username)
        self.click_continue()
        self.fill_password(password)
        self.click_login()

    def fill_username(self, username):
        time.sleep(2)
        self.driver.find_element(*AmazonLoginPageLocators.INPUT_EMAIL).send_keys(username)
        logger.info("Username Field Is Filled: ", username)

    def fill_password(self, password):
        time.sleep(2)
        self.driver.find_element(*AmazonLoginPageLocators.INPUT_PASSWORD).send_keys(password)
        logger.info("Password Field Is Filled: ", password)

    def click_continue(self):
        time.sleep(2)
        self.driver.find_element(*AmazonLoginPageLocators.BTN_CONTINUE).click()
        logger.info('Continue Button Is Clicked')

    def click_login(self):
        time.sleep(2)
        self.driver.find_element(*AmazonLoginPageLocators.BTN_LOGIN).click()
        logger.info('Login Button Is Clicked')
