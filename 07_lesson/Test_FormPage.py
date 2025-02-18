from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.alert import Alert
from FormPage import FormPage

import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get ('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    yield driver
    driver.quit()

def test_input (driver):
    form = FormPage (driver)
    form.search_first_name ("Иван")
    form.search_last_name ("Петров")
    form.search_adress ("Ленина, 55-3")
    form.search_email ("test@skypro.com")
    form.search_phone ("+7985899998787")
    form.search_country ("Россия")
    form.search_city ("Москва")
    form.search_job ("QA")
    form.search_company ("SkyPro")
    form.search_subbmit ()
    
    
    assert "success" in form.search_first_name_res ()
    assert "success" in form.search_last_name_res ()
    assert "success" in form.search_adress_res ()
    assert "success" in form.search_email_res ()
    assert "success" in form.search_phone_res ()
    assert "success" in form.search_country_res ()
    assert "success" in form.search_city_res ()
    assert "success" in form.search_job_res ()
    assert "success" in form.search_company_res ()
    assert "danger" in form.search_zip_code_res ()