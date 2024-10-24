import allure
from pages.base_page import BasePage
from pages.locators.locators import SalePage as loc


@allure.suite('Sale page')
class SalePage(BasePage):
    relative_url = 'sale.html'

    @allure.step('Check header sale')
    def check_header_sale(self):
        header_sale = self.find(loc.HEADER_SALE)
        assert header_sale.text == 'Sale'

    @allure.step('Check image promo block')
    def check_image_promo_block(self):
        img_promo_block = self.find(loc.IMG_PROMO)
        assert img_promo_block

    @allure.step('Check my wish list')
    def check_my_wish_list(self):
        my_wish_list = self.find(loc.MY_WISH_LIST)
        assert my_wish_list
