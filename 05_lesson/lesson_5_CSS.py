from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get ("http://uitestingplayground.com/classattr")

sleep(10)

driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

sleep(3)

alert = Alert(driver)
alert.accept()

sleep(3)