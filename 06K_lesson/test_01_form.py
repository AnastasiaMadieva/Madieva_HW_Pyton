from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

import pytest

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(40)
driver.get ('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

driver.maximize_window()

first_name = driver.find_element(By.NAME, "first-name")
first_name.send_keys ("Иван")

last_name = driver.find_element(By.NAME, "last-name")
last_name.send_keys ("Петров")

address = driver.find_element(By.NAME, "address")
address.send_keys ("Ленина, 55-3")

e_mail = driver.find_element(By.NAME, "e-mail")
e_mail.send_keys ("test@skypro.com")

phone = driver.find_element(By.NAME, 'phone')
phone.send_keys ("+7985899998787")

city = driver.find_element(By.NAME, 'city')
city.send_keys ("Москва")

country = driver.find_element(By.NAME, 'country')
country.send_keys ("Россия")

job = driver.find_element(By.NAME, 'job-position')
job.send_keys ("QA")

company = driver.find_element(By.NAME, 'company')
company.send_keys ("SkyPro")

subbmit = driver.find_element(By.CSS_SELECTOR, '.mt-3')
subbmit.click()

def test_01_form():
    assert "danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

def test_02_form():
    assert "success" in driver.find_element(By.ID, "first-name").get_attribute("class")

def test_03_form():
    assert "success" in driver.find_element(By.ID, "last-name").get_attribute("class")

def test_04_form():
    assert "success" in driver.find_element(By.ID, "address").get_attribute("class")

def test_05_form():
    assert "success" in driver.find_element(By.ID, "e-mail").get_attribute("class")

def test_06_form():
    assert "success" in driver.find_element(By.ID, "phone").get_attribute("class")    

def test_07_form():
    assert "success" in driver.find_element(By.ID, "city").get_attribute("class")

def test_08_form():
    assert "success" in driver.find_element(By.ID, "country").get_attribute("class")

def test_09_form():
    assert "success" in driver.find_element(By.ID, "job-position").get_attribute("class")    

def test_10_form():
    assert "success" in driver.find_element(By.ID, "company").get_attribute("class")


