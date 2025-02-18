from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from Basket import Basket

import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.get ("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_basket (driver):  
    bask = Basket (driver)
    bask.input_user_name('standard_user')
    bask.input_password('secret_sauce')
    bask.click_login_btn()
    bask.search_backpack ()    
    bask.search_bolt_t_shirt()
    bask.search_onesise()
    bask.search_shopping_cart_badge()
    bask.search_checkout()
    bask.input_first_name ('Анастасия')
    bask.input_last_name ('Мадиева')
    bask.input_postal_code ('452862')
    bask.click_continue()

    assert bask.sum_total() == 'Total: $58.29'