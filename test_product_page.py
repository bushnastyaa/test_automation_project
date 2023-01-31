import pytest
from .pages.product_page import ProductPage


@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, index):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{index}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()

    page.get_name_of_product()
    page.get_price_of_product()

    page.add_to_basket_button()
    page.solve_quiz_and_get_code()

    page.item_should_be_added()
    page.item_price_should_be_equal()
