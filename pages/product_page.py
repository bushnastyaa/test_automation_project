from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to basket button is not presented'

    def add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_name_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PRICE).text

    def item_should_be_added(self):
        added_item_text = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        assert self.get_name_of_product() == added_item_text, 'Item is not added to basket'

    def item_price_should_be_equal(self):
        price = self.browser.find_element(*ProductPageLocators.TOTAL_COST_OF_BASKET_MESSAGE).text
        assert self.get_price_of_product() == price, 'Price does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message should not be presented on product page"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message should be desappeared on product page"