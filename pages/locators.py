from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    TOTAL_COST_OF_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")
