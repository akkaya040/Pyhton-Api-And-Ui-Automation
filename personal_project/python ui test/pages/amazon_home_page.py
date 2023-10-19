from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePageLocators
from utils.CustomLogger import CustomLogger
import time
logger = CustomLogger()


class AmazonHomePageLocators(BasePageLocators):
    BTN_ACCOUNT_LOGIN = (By.CSS_SELECTOR, "a[id='nav-link-accountList']")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    TXT_PRODUCTS = (By.CSS_SELECTOR, "span[class='a-size-base-plus a-color-base a-text-normal']")
    TXT_PRODUCT_TITLE = (By.CSS_SELECTOR, "span[id='productTitle']")
    TXT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".reinventPricePriceToPayMargin  span.a-offscreen")
    BTN_ADD_BASKET = (By.ID, "add-to-cart-button")
    BTN_BASKET = (By.ID, "nav-cart-text-container")


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_keyword(self, keyword):
        logger.info("Searching Is Progress ", keyword)
        self.fill_search_field(keyword)
        self.press_return_key()

    def fill_search_field(self, keyword):
        time.sleep(2)
        self.driver.find_element(*AmazonHomePageLocators.SEARCH_BOX).send_keys(keyword)
        logger.info(keyword + ' Is Filled To  Searchbox ')

    def press_return_key(self):
        time.sleep(2)
        self.driver.find_element(*AmazonHomePageLocators.SEARCH_BOX).send_keys(Keys.RETURN)
        logger.info('Pressing Enter For Continue Search')

    def click_login_button_tabbar(self):
        time.sleep(2)
        self.driver.find_element(*AmazonHomePageLocators.BTN_ACCOUNT_LOGIN).click()

    def click_first_product(self):
        time.sleep(2)
        product = self.driver.find_elements(*AmazonHomePageLocators.TXT_PRODUCTS)[0]
        title = product.text
        logger.info('Product Title Will Be Clicked: ', title)
        product.click()
        return title

    def get_product_detail_title(self):
        time.sleep(2)
        title = self.driver.find_element(*AmazonHomePageLocators.TXT_PRODUCT_TITLE).text
        logger.info('Product Detail Title Is Viewed: ', title)
        return title

    def add_product_to_basket(self):
        time.sleep(2)
        product_detail_price = self.driver.find_element(*AmazonHomePageLocators.TXT_PRODUCT_PRICE).text
        logger.info("Product Price In Detail: ", product_detail_price)
        self.driver.find_element(*AmazonHomePageLocators.BTN_ADD_BASKET).click()
        return product_detail_price

    def go_to_basket_page(self):
        time.sleep(2)
        self.driver.find_element(*AmazonHomePageLocators.BTN_BASKET).click()
