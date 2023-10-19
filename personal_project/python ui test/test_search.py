import sys
import unittest

from utils.BrowserUtils import BrowserUtils
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_login_page import AmazonLoginPage
from pages.amazon_basket_page import AmazonBasketPage
from utils.CustomLogger import CustomLogger

logger = CustomLogger()


class TestSearch(unittest.TestCase):
    def setUp(self):
        logger.info('setUp()')
        logger.info('Tests have been started...')
        self.driver = BrowserUtils().get_browser(sys.argv[1])
        self.browser = sys.argv[1]
        self.keyword = sys.argv[2]
        self.username = sys.argv[3]
        self.password = sys.argv[4]

    def test_search_amazon(self):
        logger.info('test_search_amazon()')
        hp = AmazonHomePage(self.driver)
        lp = AmazonLoginPage(self.driver)
        bp = AmazonBasketPage(self.driver)

        hp.driver.get("https://www.amazon.com.tr")
        # hp.click_login_button_tabbar()
        # lp.login_with_given_user_and_pass(self.username, self.password)
        hp.search_for_keyword(self.keyword)
        expected_product_title = hp.click_first_product()
        actual_product_title = hp.get_product_detail_title()

        if expected_product_title == actual_product_title:
            logger.info("Clicked Product And Product Detail Are Matched")
        else:
            logger.error("Clicked Product And Product Detail Are Not Matched!")

        product_detail_price = hp.add_product_to_basket()
        hp.go_to_basket_page()
        total_basket_price = bp.get_basket_total_price()

        self.assertEqual(product_detail_price, total_basket_price, "Prices Are Different")

    def tearDown(self):
        logger.info('tearDown()')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
