from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get ("http://the-internet.herokuapp.com/login")

sleep(5)

input_username = driver.find_element(By.CSS_SELECTOR, '#username')
input_username.send_keys ("tomsmith")

sleep(2)

input_password = driver.find_element(By.CSS_SELECTOR, '#password')
input_password.send_keys ("SuperSecretPassword!")

sleep(2)

driver.find_element(By.CSS_SELECTOR, 'i.fa').click()

sleep(3)


driver.quit()