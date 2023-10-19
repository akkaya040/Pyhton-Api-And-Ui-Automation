from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePageLocators
from utils.CustomLogger import CustomLogger
import time
logger = CustomLogger()


class AmazonBasketPageLocators(BasePageLocators):
    TXT_CARD_PRICE = (By.ID, "sc-subtotal-amount-buybox")


class AmazonBasketPage:
    def __init__(self, driver):
        self.driver = driver

    def get_basket_total_price(self):
        time.sleep(2)
        card_price = self.driver.find_element(*AmazonBasketPageLocators.TXT_CARD_PRICE).text
        logger.info("Basket Price: ", card_price)
        return card_price
