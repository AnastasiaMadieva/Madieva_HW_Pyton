from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage:
    def __init__(self, driver):
        """
                Найти поле delay
        """
        self.driver = driver
        self.delay = (By.CSS_SELECTOR, '#delay')
        #self.btn = (By.XPATH, '//span[text()=',qwer,']')

    @allure.step ("Очистить поле delay")
    def search_delay_clear (self):
        """
                Эта функция очищает поле delay
        """
        delay_clear = self.driver.find_element(*self.delay)
        delay_clear.clear ()

    @allure.step ("Ввести в поле delay данные")
    def input_delay (self, query:int):
        """
                Эта функция вводит в поле delay данные
        """
        delay_search = self.driver.find_element(*self.delay)
        delay_search.send_keys (query)
        return delay_search
    
    @allure.step ("Нажать на кнопку {span_text}")
    def click_btn (self, span_text):
        """
                Эта функция нажимает на кнопки
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{span_text}']" ).click() 
        self.driver.implicitly_wait(1)  
    
    @allure.step ("Ожидание результата")
    def calc_wait (self):
        """
                Эта функция ожидает результат после нажатия на кнопку "="
        """
        WebDriverWait (self.driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    @allure.step("Вернуть в ответе итоговое значение")
    def calc_result (self):
        """
                Эта функция возвращает результат после нажатия на кнопку "="
        """
        txt = self.driver.find_element (By.CSS_SELECTOR, '.screen').text
        return txt
      
