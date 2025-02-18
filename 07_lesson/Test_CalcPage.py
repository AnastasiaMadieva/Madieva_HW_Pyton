from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
from CalkPage import CalcPage

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
    calc.search_delay ("45")
    calc.search_btn7 ()
    calc.search_btnSumm ()
    calc.search_btn8 ()
    calc.search_btnEqual ()
    calc.calc_wait()

    assert calc.calc_result () == '15'