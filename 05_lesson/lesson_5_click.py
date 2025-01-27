from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get ("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range (0,5):
    driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click ()

delete_element = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print ("Кнопок 'Delete'", len(delete_element))


sleep (10)