from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
from calkPage import CalcPage

import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(20)
    driver.get ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calk(driver):
    calc = CalcPage (driver)
    calc.search_delay_clear ()
    calc.input_delay (45)
    calc.click_btn ('7')
    calc.click_btn ('+')
    calc.click_btn ('8')
    calc.click_btn ('=')
    calc.calc_wait()

    assert calc.calc_result () == '15'