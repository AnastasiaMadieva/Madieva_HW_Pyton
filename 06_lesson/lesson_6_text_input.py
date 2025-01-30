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

driver.get ("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

new_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
new_btn.click()
txt = new_btn.text
print (f"Новое название кнопки '{txt}'")
