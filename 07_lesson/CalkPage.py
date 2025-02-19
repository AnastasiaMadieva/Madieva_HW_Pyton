from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay = (By.CSS_SELECTOR, '#delay')
        #self.btn = (By.XPATH, '//span[text()=',qwer,']')


    def search_delay_clear (self):
        delay_clear = self.driver.find_element(*self.delay)
        delay_clear.clear ()

    def input_delay (self, query):
        delay_search = self.driver.find_element(*self.delay)
        delay_search.send_keys (query)
        return delay_search
    
    def click_btn (self, span_text):
        self.driver.find_element(By.XPATH, f"//span[text()='{span_text}']" ).click() 
        self.driver.implicitly_wait(1)  
    

    def calc_wait (self):
        WebDriverWait (self.driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    def calc_result (self):
        txt = self.driver.find_element (By.CSS_SELECTOR, '.screen').text
        return txt
      
