from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get ("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys ('standard_user')

driver.find_element(By.CSS_SELECTOR, '#password').send_keys ('secret_sauce')

driver.find_element(By.CSS_SELECTOR, '#login-button').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').click()

driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys ('Анастасия')

driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys ('Мадиева')

driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys ('452862')

driver.find_element(By.CSS_SELECTOR, '#continue').click()

def test_total():
    txt = driver.find_element (By.CSS_SELECTOR, '.summary_total_label').text
    print (f'Итоговая сумма к оплате {txt}')
    assert txt == 'Total: $58.29'