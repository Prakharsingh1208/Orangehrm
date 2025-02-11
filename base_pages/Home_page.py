import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.config_reader import ReadConfig_menu, ReadConfig_contact_form
from utilities.custom_log import Log_gen
class Home_page_menu:
    # url = ReadConfig_menu.get_application_url()
    # demo_booking = ReadConfig_menu.get_booking_button()
    # contact_sales = ReadConfig_menu.get_contact_sales_button()
    log = Log_gen.create_log()

    def __init__(self,driver):
        self.driver = driver

    def open_home_page(self,url):
        self.driver.maximize_window()
        self.log.info("[+] Opening the home page")
        self.driver.get(url)
        
    def Accept_cookie(self,button):
        self.log.info("[+] Clicking on Accept cookie button")
        self.driver.find_element(By.XPATH,button).click()

    
    def click_booking_button(self,demo_booking):
        self.log.info("[+] Clicking the demo booking buttton")
        self.driver.find_element(By.XPATH,demo_booking).click()

    def click_contact_sales_button(self,contact_sales):
        self.log.info("[+] Clicking the contact sales button")
        self.driver.find_element(By.XPATH,contact_sales).click()

class form_filling:
    log = Log_gen.create_log()

    def __init__(self,driver):
        self.driver = driver
        
    def enter_name(self,name):
        self.log.info("[+] Entering the name")
        self.driver.find_element(By.XPATH,name).send_keys("Prakhar singh")
    
    def enter_phone_number(self,phone_number):
        self.log.info("[+] Entering the phone number")
        self.driver.find_element(By.XPATH,phone_number).send_keys("+918087613881")

    def enter_email(self,email):
        self.log.info("[+] Entering the Email")
        self.driver.find_element(By.XPATH,email).send_keys("prakharsingh1208@gmail.com")

    def enter_phone_number(self,phone_number):
        self.log.info("[+] Entering the phone number")
        self.driver.find_element(By.XPATH,phone_number).send_keys("+918087613881")

    def enter_country(self,country):
        self.log.info("[+] Entering the country")
        option = self.driver.find_element(By.XPATH,country)
        select = Select(option)
        select.select_by_visible_text("India")
        
    def enter_no_of_employe(self,number):
        self.log.info("[+] Entering the number of employe")
        option = self.driver.find_element(By.XPATH,number)
        select = Select(option)
        select.select_by_value("51 - 200")
    
    def enter_company(self,company):
        self.log.info("[+] Entering the company")
        self.driver.find_element(By.XPATH,company).send_keys("Browserstack")
    
    def submit(self,submite_button):
        self.log.info("[+] Submitting the form")
        self.driver.find_element(By.ID,submite_button).click()
    
    def job_title(self,job_title):
        self.log.info("[+] Entering the job title")
        self.driver.find_element(By.XPATH,job_title).send_keys("SDET")

    def your_message(self,your_message):
        self.log.info("[+] Entering your meassage")
        self.driver.find_element(By.XPATH,your_message).send_keys("Hello Wordl!")

    def test_verification_demo_contact(self):
        if self.driver.current_url == "https://www.orangehrm.com/en/book-a-free-demo/demo-confirmation":
            self.log.info("[+] Test case 03 passed")
            self.driver.quit()
            assert True
        else:
            self.log.info("[+] Test case 03 failed")
            self.driver.quit()
            assert False
    def test_negative_verification_demo_contact(self):
        if self.driver.current_url == "https://www.orangehrm.com/en/book-a-free-demo/demo-confirmation":
            self.log.info("[+] Test case 05 Failed")
            self.driver.quit()
            assert True
        else:
            self.log.info("[+] Test case 05 Passed")
            self.driver.quit()
            assert False

    def test_verification_sales_contact(self):
        if self.driver.current_url == "https://www.orangehrm.com/en/contact-sales/success":
            self.log.info("[+] Test case 02 passed")
            self.driver.quit()
            assert False
        else:
            self.log.info("[+] Test case 02 Failed")
            self.driver.quit()
            assert True
    
    def test_negative_verification_sales_contact(self):
        if self.driver.current_url == "https://www.orangehrm.com/en/contact-sales/success":
            self.log.info("[+] Test case 04 Failed")
            self.driver.quit()
            assert False
        else:
            self.log.info("[+] Test case 04 Passed")
            self.driver.quit()
            assert True

    