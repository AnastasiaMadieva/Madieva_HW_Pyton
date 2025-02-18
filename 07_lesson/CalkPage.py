from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay = (By.CSS_SELECTOR, '#delay')
        self.btn7 = (By.XPATH, '//span[text()="7"]')
        self.btnSumm = (By.XPATH, '//span[text()="+"]')
        self.btn8 = (By.XPATH, '//span[text()="8"]')
        self.btnEqual = (By.XPATH, '//span[text()="="]')

    def search_delay_clear (self):
        delay_clear = self.driver.find_element(*self.delay)
        delay_clear.clear ()

    def search_delay (self, query):
        delay_search = self.driver.find_element(*self.delay)
        delay_search.send_keys (query)

    def search_btn7 (self):
        self.driver.find_element(*self.btn7).click()   

    def search_btnSumm (self):
        self.driver.find_element(*self.btnSumm).click() 

    def search_btn8 (self):
        self.driver.find_element(*self.btn8).click() 

    def search_btnEqual (self):
        self.driver.find_element(*self.btnEqual).click()        

    def calc_wait (self):
        WebDriverWait (self.driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    def calc_result (self):
        txt = self.driver.find_element (By.CSS_SELECTOR, '.screen').text
        return txt
        #assert txt == '15'
