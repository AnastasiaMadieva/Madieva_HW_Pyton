from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.NAME, "first-name")
        #self.first_name.send_keys ("Иван")
        self.last_name = (By.NAME, "last-name")
        #self.last_name.send_keys ("Петров")
        self.address = (By.NAME, "address")
        #self.address.send_keys ("Ленина, 55-3")
        self.e_mail = (By.NAME, "e-mail")
        #self.e_mail.send_keys ("test@skypro.com")
        self.phone = (By.NAME, 'phone')
        #self.phone.send_keys ("+7985899998787")
        self.city = (By.NAME, 'city')
        #self.city.send_keys ("Москва")
        self.country = (By.NAME, 'country')
        #self.country.send_keys ("Россия")
        self.job = (By.NAME, 'job-position')
        #self.job.send_keys ("QA")
        self.company = (By.NAME, 'company')
        #self.company.send_keys ("SkyPro")
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


    def search_first_name (self, f_n):
        search_first_name_element = self.driver.find_element(*self.first_name)
        search_first_name_element.send_keys(f_n)

    def search_last_name (self, l_n):
        search_last_name_element = self.driver.find_element(*self.last_name)
        search_last_name_element.send_keys(l_n)

    def search_adress (self, adr):
        search_adress_element = self.driver.find_element(*self.address)
        search_adress_element.send_keys(adr)

    def search_email (self, mail):
        search_email_element = self.driver.find_element(*self.e_mail)
        search_email_element.send_keys(mail)

    def search_phone (self, tel):
        search_phone_element = self.driver.find_element(*self.phone)
        search_phone_element.send_keys(tel)

    def search_city (self, gorod):
        search_city_element = self.driver.find_element(*self.city)
        search_city_element.send_keys(gorod)

    def search_country (self, strana):
        search_country_element = self.driver.find_element(*self.country)
        search_country_element.send_keys(strana)

    def search_job (self, rabota):
        search_job_element = self.driver.find_element(*self.job)
        search_job_element.send_keys(rabota)
    
    def search_company (self, query):
        search_company_element = self.driver.find_element(*self.company)
        search_company_element.send_keys(query)

    
    def search_subbmit (self):
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
