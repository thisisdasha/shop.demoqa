import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = "http://shop.demoqa.com/"
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

class TestSearch():
    @pytest.mark.parametrize('tested_string', ["dress", "coat", "shoes"])
    def test_search_on_main_page(self, browser, tested_string):
        browser.get(link)
        button_search = browser.find_element_by_css_selector('i[class="icon_search"]')
        button_search.click()
        input_search = browser.find_element_by_css_selector('input[type="search"]')
        input_search.send_keys(tested_string)
        input_search.send_keys(Keys.ENTER)
        assert tested_string in browser.current_url
        assert "results" in browser.find_element_by_css_selector('p[class="woocommerce-result-count"]').text
