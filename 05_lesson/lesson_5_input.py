from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get ("http://the-internet.herokuapp.com/inputs")

sleep(5)

input_box = driver.find_element(By.CSS_SELECTOR, 'input')
input_box.send_keys (1000)

sleep(3)
input_box.clear()
sleep(2)
input_box.send_keys(999)
sleep(3)


driver.quit()