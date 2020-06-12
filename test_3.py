import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://shop.demoqa.com/my-account/"
username = "DariaTok"
pwd = "My_password-2"
email = "new02.email@gmail.com"


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAddToCart():
    @pytest.mark.skip
    def test_login_and_go_to_cart(self, browser):
        browser.get(link)
        input_username = browser.find_element_by_css_selector('[id="username"]')
        input_username.send_keys(username)
        input_pwd = browser.find_element_by_css_selector('[name="password"]')
        input_pwd.send_keys(pwd)
        button_log_in = browser.find_element_by_css_selector('[name="login"]')
        button_log_in.click()
        greeting = browser.find_element_by_css_selector('strong')
        time.sleep(2)
        assert username in greeting.text

        button_cart = browser.find_element_by_class_name("cart-name-and-total")
        button_cart.click()
        assert browser.current_url == "http://shop.demoqa.com/cart/"


    def test_check_empty_cart(self, browser):
        TestAddToCart.test_login_and_go_to_cart(TestAddToCart, browser)
        message_empty = browser.find_element_by_css_selector('p')
        if "empty" in message_empty.text:
            print("Cart is empty...")
            button_return_to_shop = browser.find_element_by_css_selector("[class='button wc-backward']")
            button_return_to_shop.click()
            assert browser.current_url == "http://shop.demoqa.com/shop/"
            first_product = browser.find_element_by_css_selector('h3')
            first_product.click()
            assert browser.current_url != "http://shop.demoqa.com/shop/"
            button_color1 = browser.find_element_by_css_selector('select[id="pa_color"]')
            button_color1.click()
            button_color2 = browser.find_element_by_css_selector('option[value="black"]')
            button_color2.click()
            button_size1 = browser.find_element_by_css_selector('select[id="pa_size"]')
            button_size1.click()
            button_size2 = browser.find_element_by_css_selector('option[value="small"]')
            button_size2.click()
            button_add_to_cart = browser.find_element_by_css_selector(
                'button[class="single_add_to_cart_button button alt"]')
            button_add_to_cart.click()
            message_added_to_cart = browser.find_element_by_css_selector('div[class="woocommerce-message"]')
            assert "added to your cart" in message_added_to_cart.text
            print("Product added successfully...")
        else:
            print("Cart not Empty")
        browser.get("http://shop.demoqa.com/cart/")
        assert browser.find_element_by_css_selector('th[class="product-thumbnail"]').text.lower() == "product"

    def test_check_for_saving_changes_after_relogin(self, browser):
        TestAddToCart.test_check_empty_cart(TestAddToCart, browser)
        browser.get("http://shop.demoqa.com/my-account/")
        button_logout = browser.find_element_by_xpath("//*[contains(text(), 'Log out')]")
        button_logout.click()
        assert browser.find_element_by_xpath("//*[contains(text(), 'Login')]").text.lower() == "login"
        TestAddToCart.test_login_and_go_to_cart(TestAddToCart, browser)
        assert browser.find_element_by_css_selector('th[class="product-thumbnail"]').text.lower() == "product"



