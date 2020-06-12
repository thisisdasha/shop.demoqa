import pytest
from selenium import webdriver
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


class TestPayment():
    @pytest.mark.skip
    def test_go_to_payment_page_with_login(self, browser):
        browser.get(link)
        input_username = browser.find_element_by_css_selector('[id="username"]')
        input_username.send_keys(username)
        input_pwd = browser.find_element_by_css_selector('[name="password"]')
        input_pwd.send_keys(pwd)
        button_log_in = browser.find_element_by_css_selector('[name="login"]')
        button_log_in.click()
        greeting = browser.find_element_by_css_selector('strong')
        assert username in greeting.text
        browser.get("http://shop.demoqa.com/cart/")
        button_proceed_to_checkout = browser.find_element_by_css_selector(
            'a[class="checkout-button button alt wc-forward"]')
        button_proceed_to_checkout.click()
        time.sleep(5)
        assert browser.current_url == "http://shop.demoqa.com/checkout/"

    def test_place_order_with_filling(self, browser):
        TestPayment.test_go_to_payment_page_with_login(TestPayment, browser)
        input_name = browser.find_element_by_id('billing_first_name')
        input_name.send_keys("Daria")
        input_last_name = browser.find_element_by_id('billing_last_name')
        input_last_name.send_keys("Tokareva")
        input_street1 = browser.find_element_by_id('billing_address_1')
        input_street1.send_keys('Safonovo')
        input_street2 = browser.find_element_by_id('billing_address_2')
        input_street2.send_keys('1')
        input_city = browser.find_element_by_id('billing_city')
        input_city.send_keys('Murmansk')
        input_country = browser.find_element_by_id('billing_state')
        input_country.send_keys('Russia')
        input_postcode = browser.find_element_by_id('billing_postcode')
        input_postcode.send_keys('184621')
        input_phone = browser.find_element_by_css_selector('input[type="tel"]')
        input_phone.send_keys("89113031232")
        time.sleep(5)
        cb = browser.find_element_by_css_selector("input[type='checkbox']")
        cb.click()
        button_place_order = browser.find_element_by_css_selector('button[value="Place order"]')
        button_place_order.click()
        time.sleep(5)
        assert browser.current_url != "http://shop.demoqa.com/checkout/"


