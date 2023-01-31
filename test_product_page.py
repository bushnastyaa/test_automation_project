import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from pages.login_page import LoginPage


class TestAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_button()

        page.get_name_of_product()
        page.get_price_of_product()

        page.add_to_basket_button()
        page.solve_quiz_and_get_code()

        page.item_should_be_added()
        page.item_price_should_be_equal()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.success_message_should_disappeared()


@pytest.mark.temp_marker
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_page_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_button()

        page.get_name_of_product()
        page.get_price_of_product()

        page.add_to_basket_button()
        page.solve_quiz_and_get_code()

        page.item_should_be_added()
        page.item_price_should_be_equal()


class TestCanGoToLoginPageFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


@pytest.mark.go_to_basket
class TestGoToBasketFromProductPage():
    def test_guest_should_see_basket_button_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_is_empty_text()
        basket_page.should_not_be_basket_items_element()
