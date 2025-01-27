from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get ("http://the-internet.herokuapp.com/entry_ad")

sleep(10)

driver.find_element(By.CSS_SELECTOR, 'div.modal-footer > p').click()

sleep(3)

driver.quit()