from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.implicitly_wait(20)
 
element = WebDriverWait(driver, 40)
images = element.until (EC.presence_of_all_elements_located ((By.CSS_SELECTOR, 'div#image-container')))

src = driver.find_element (By.CSS_SELECTOR, "#award").get_attribute("src")

print(f"Путь картинке 3 {src}")


driver.quit()