from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import allure




class Basket:   
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.CSS_SELECTOR, '#user-name')
        self.password = (By.CSS_SELECTOR, '#password')
        self.login_button = (By.CSS_SELECTOR, '#login-button')
        self.backpack = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
        self.bolt_t_shirt = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
        self.onesise = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
        self.shopping_cart_badge = (By.CSS_SELECTOR, '.shopping_cart_badge')
        self.checkout = (By.CSS_SELECTOR, '#checkout')
        self.first_name = (By.CSS_SELECTOR, '#first-name')
        self.last_name = (By.CSS_SELECTOR, '#last-name')
        self.postal_code = (By.CSS_SELECTOR, '#postal-code')
        self.resume = (By.CSS_SELECTOR, '#continue')

    @allure.step("Ввести Имя пользователя в поле Имя пользователя")
    def input_user_name (self, u):
        self.driver.find_element (*self.user_name).send_keys(u)

    @allure.step("Ввести Пароль в поле пароль")
    def input_password (self, pasw):
        self.driver.find_element (*self.password).send_keys(pasw)

    @allure.step("Нажать на кнопку авторизации")
    def click_login_btn(self):
        self.driver.find_element (*self.login_button).click ()

    @allure.step("выбрать продукт backpack")
    def search_backpack (self):
        self.driver.find_element (*self.backpack).click () 

    @allure.step("выбрать продукт bolt_t_shirt")
    def search_bolt_t_shirt (self):
        self.driver.find_element (*self.bolt_t_shirt).click () 

    @allure.step("выбрать продукт onesise")
    def search_onesise (self):
        self.driver.find_element (*self.onesise).click () 

    @allure.step("перейти в корзину")
    def search_shopping_cart_badge (self):
        self.driver.find_element (*self.shopping_cart_badge).click ()    

    @allure.step("нажать на кнопку checkout")
    def search_checkout (self):
        self.driver.find_element (*self.checkout).click () 
        
    @allure.step("Ввести Имя в поле Имя")
    def input_first_name (self, first_n):
        self.driver.find_element (*self.first_name).send_keys(first_n) 

    @allure.step("Ввести Фамилию в поле Фамилия")
    def input_last_name (self, last_n):
        self.driver.find_element (*self.last_name).send_keys(last_n)            

    @allure.step("Ввести Почтовый индекс в поле postal_code")
    def input_postal_code (self, cod):
        self.driver.find_element (*self.postal_code).send_keys(cod) 

    @allure.step("Нажать на кнопку continue")
    def click_continue (self):
        self.driver.find_element (*self.resume).click ()     

    
    @allure.step("Вернуть в ответе итоговую сумму")
    def sum_total(self):
        txt = self.driver.find_element (By.CSS_SELECTOR, '.summary_total_label').text
        return txt
    