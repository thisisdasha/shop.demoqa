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


class TestPersonalAccount():
    @pytest.mark.skip
    def test_login_without_password(self, browser):
        browser.get(link)
        input_username = browser.find_element_by_css_selector('[id="username"]')
        input_username.send_keys(username)
        button_log_in = browser.find_element_by_css_selector('[name="login"]')
        button_log_in.click()
        error_message = browser.find_element_by_css_selector('strong')
        assert "ERROR" in error_message.text

    @pytest.mark.skip
    def test_login_without_username(self, browser):
        browser.get(link)
        input_pwd = browser.find_element_by_css_selector('[name="password"]')
        input_pwd.send_keys(pwd)
        button_log_in = browser.find_element_by_css_selector('[name="login"]')
        button_log_in.click()
        error_message = browser.find_element_by_css_selector('strong')
        assert "Error" in error_message.text

    @pytest.mark.skip
    def test_login(self, browser):
        browser.get(link)
        input_username = browser.find_element_by_css_selector('[id="username"]')
        input_username.send_keys(username)
        input_pwd = browser.find_element_by_css_selector('[name="password"]')
        input_pwd.send_keys(pwd)
        button_log_in = browser.find_element_by_css_selector('[name="login"]')
        button_log_in.click()
        greeting = browser.find_element_by_css_selector('strong')
        assert username in greeting.text

    def test_login_invalid_input(self, browser):
        browser.get(link)
        input_username = browser.find_element_by_css_selector('[id="username"]')
        input_username.send_keys("InvalidUsername")
        input_pwd = browser.find_element_by_css_selector('[name="password"]')
        input_pwd.send_keys(pwd)
        button_log_in = browser.find_element_by_css_selector('[name="login"]')
        button_log_in.click()
        greeting = browser.find_element_by_css_selector('strong')
        assert "ERROR" in greeting.text
