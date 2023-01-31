from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT), "'Basket-is-empty' text is not presented on basket page"

    def should_not_be_basket_items_element(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS_ELEMENT), "Items should not be presented on basket page"
