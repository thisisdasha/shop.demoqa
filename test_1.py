import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://shop.demoqa.com/"


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestNewUser():
    @pytest.mark.xfail
    def test_guest_go_to_my_account(self, browser):
        browser.get(link)
        button_my_account = browser.find_element_by_css_selector('[href="http://shop.demoqa.com/my-account/"]')
        button_my_account.click()

    def test_guest_go_to_my_account_after_scrolling(self, browser):
        browser.get(link)
        button_my_account = browser.find_element_by_css_selector('[href="http://shop.demoqa.com/my-account/"]')
        browser.execute_script("window.scrollBy(0,200);")
        button_my_account.click()

    def test_new_user_registration_without_password(self, browser):
        browser.get(link + "my-account/")
        input_username = browser.find_element_by_css_selector('[id="reg_username"]')
        input_username.send_keys("Daria")
        input_email = browser.find_element_by_css_selector('[type="email"]')
        input_email.send_keys("some.email@gmail.com")
        button_register = browser.find_element_by_css_selector('[name="register"]')
        button_register.click()
        error_message = browser.find_element_by_css_selector('strong')
        assert "Error" in error_message.text

    def test_new_user_registration_without_name(self, browser):
        browser.get(link + "my-account/")
        input_email = browser.find_element_by_css_selector('[type="email"]')
        input_email.send_keys("some.email@gmail.com")
        input_password = browser.find_element_by_css_selector('[id="reg_password"]')
        input_password.send_keys("My_password-25")
        button_register = browser.find_element_by_css_selector('[name="register"]')
        button_register.click()
        error_message = browser.find_element_by_css_selector('strong')
        assert "Error" in error_message.text

    def test_new_user_registration_without_email(self, browser):
        browser.get(link + "my-account/")
        input_username = browser.find_element_by_css_selector('[id="reg_username"]')
        input_username.send_keys("Daria")
        input_password = browser.find_element_by_css_selector('[id="reg_password"]')
        input_password.send_keys("My_password-25")
        button_register = browser.find_element_by_css_selector('[name="register"]')
        button_register.click()
        error_message = browser.find_element_by_css_selector('strong')
        assert "Error" in error_message.text

    def test_new_user_registration(self, browser):
        username = "DariaTok"
        pwd = "My_password-2"
        email = "new02.email@gmail.com"
        browser.get(link + "my-account/")
        input_username = browser.find_element_by_css_selector('[id="reg_username"]')
        input_username.send_keys(username)
        input_email = browser.find_element_by_css_selector('[type="email"]')
        input_email.send_keys(email)
        input_password = browser.find_element_by_css_selector('[id="reg_password"]')
        input_password.send_keys(pwd)
        button_register = browser.find_element_by_css_selector('[name="register"]')
        button_register.click()
        assert browser.current_url == "http://shop.demoqa.com/shop-demoqa?redirect_to=http%3A%2F%2Fshop.demoqa.com%2Fmy-account%2F&aiowps_login_msg_id=session_expired"
        input_login_name = browser.find_element_by_css_selector('[id="user_login"]')
        input_login_password = browser.find_element_by_css_selector('[name="pwd"]')
        input_login_name.send_keys(username)
        input_login_password.send_keys(pwd)
        button_login = browser.find_element_by_css_selector('[type="submit"]')
        button_login.click()
        assert browser.current_url == "http://shop.demoqa.com/my-account/"
