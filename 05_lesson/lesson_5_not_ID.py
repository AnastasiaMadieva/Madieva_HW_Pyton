from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get ("http://uitestingplayground.com/dynamicid")

for x in range (0,3):
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click ()



sleep (10)