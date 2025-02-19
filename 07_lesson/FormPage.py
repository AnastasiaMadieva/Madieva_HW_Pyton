from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.NAME, "first-name")
        self.last_name = (By.NAME, "last-name")
        self.address = (By.NAME, "address")
        self.e_mail = (By.NAME, "e-mail")
        self.phone = (By.NAME, 'phone')
        self.city = (By.NAME, 'city')
        self.country = (By.NAME, 'country')
        self.job = (By.NAME, 'job-position')
        self.company = (By.NAME, 'company')
        self.subbmit = (By.CSS_SELECTOR, '.mt-3')

        self.first_name_result = (By.ID, "first-name")
        self.last_name_result = (By.ID, "last-name")
        self.address_result = (By.ID, "address")
        self.e_mail_result = (By.ID, "e-mail")
        self.phone_result = (By.ID, 'phone')
        self.city_result = (By.ID, 'city')
        self.country_result = (By.ID, 'country')
        self.job_result = (By.ID, 'job-position')
        self.company_result = (By.ID, 'company')
        self.zip_code_result = (By.ID, 'zip-code')


    def input_first_name (self, f_n):
        search_first_name_element = self.driver.find_element(*self.first_name)
        search_first_name_element.send_keys(f_n)

    def input_last_name (self, l_n):
        search_last_name_element = self.driver.find_element(*self.last_name)
        search_last_name_element.send_keys(l_n)

    def input_adress (self, adr):
        search_adress_element = self.driver.find_element(*self.address)
        search_adress_element.send_keys(adr)

    def input_email (self, mail):
        search_email_element = self.driver.find_element(*self.e_mail)
        search_email_element.send_keys(mail)

    def input_phone (self, tel):
        search_phone_element = self.driver.find_element(*self.phone)
        search_phone_element.send_keys(tel)

    def input_city (self, gorod):
        search_city_element = self.driver.find_element(*self.city)
        search_city_element.send_keys(gorod)

    def input_country (self, strana):
        search_country_element = self.driver.find_element(*self.country)
        search_country_element.send_keys(strana)

    def input_job (self, rabota):
        search_job_element = self.driver.find_element(*self.job)
        search_job_element.send_keys(rabota)
    
    def input_company (self, query):
        search_company_element = self.driver.find_element(*self.company)
        search_company_element.send_keys(query)

    
    def click_subbmit (self):
        self.driver.find_element(*self.subbmit).click()

       
    
    def search_zip_code_res (self):
        search_zip_code_result = self.driver.find_element(*self.zip_code_result).get_attribute("class")
        return search_zip_code_result

    def search_first_name_res (self):
        search_first_name_result = self.driver.find_element(*self.first_name_result).get_attribute("class")
        return search_first_name_result
    
    def search_last_name_res (self):
        search_last_name_result = self.driver.find_element(*self.last_name_result).get_attribute("class")
        return search_last_name_result

    def search_adress_res (self):
        search_adress_result = self.driver.find_element(*self.address_result).get_attribute("class")
        return search_adress_result

    def search_email_res (self):
        search_email_result = self.driver.find_element(*self.e_mail_result).get_attribute("class")
        return search_email_result

    def search_phone_res (self):
        search_phone_result = self.driver.find_element(*self.phone_result).get_attribute("class")
        return search_phone_result

    def search_city_res (self):
        search_city_result = self.driver.find_element(*self.city_result).get_attribute("class")
        return search_city_result

    def search_country_res (self):
        search_country_result = self.driver.find_element(*self.country_result).get_attribute("class")
        return search_country_result

    def search_job_res (self):
        search_job_result = self.driver.find_element(*self.job_result).get_attribute("class")
        return search_job_result
    
    def search_company_res (self):
        search_company_result = self.driver.find_element(*self.company_result).get_attribute("class")
        return search_company_result
