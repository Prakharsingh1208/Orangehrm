import pytest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base_pages.Home_page import Home_page_menu
from base_pages.Home_page import form_filling
from utilities.config_reader import ReadConfig_menu, ReadConfig_contact_form
from utilities.custom_log import Log_gen
from test_cases import conftest

class Test:
    url = ReadConfig_menu.get_application_url()
    demo_booking = ReadConfig_menu.get_booking_button()
    contact_sales = ReadConfig_menu.get_contact_sales_button()
    cross_button = ReadConfig_menu.get_cross_button()
    name = ReadConfig_contact_form.get_name()
    phone_number = ReadConfig_contact_form.get_phone_number()
    email = ReadConfig_contact_form.get_email()
    country = ReadConfig_contact_form.get_country()
    no_of_employe = ReadConfig_contact_form.get_number_of_employes()
    company = ReadConfig_contact_form.get_company_name()
    #recaptcha = ReadConfig_contact_form.get_recaptcha()
    submite_button = ReadConfig_contact_form.get_contact_sales()
    job_title = ReadConfig_contact_form.get_job_title()
    your_message = ReadConfig_contact_form.get_your_message() 
    log = Log_gen.create_log()

    def test_01_title_verification(self,setup):
        self.log.info("-----------------Test-01------------------")
        self.driver = setup
        browser = Home_page_menu(self.driver)
        browser.open_home_page(self.url)
        if self.driver.title == "Human Resources Management Software | OrangeHRM 1":
            self.log.info("[+] Test case 01 Passed")
            self.driver.quit()
            assert True
        else:
            self.log.info("[+] Test case 01 Failed")
            self.driver.save_screenshot(r"C:\Users\pranj\OneDrive\Desktop\Orangehrm\screenshots\test_01.png")
            self.driver.quit()
            assert False
    
    def test_02_positive_verfication_of_sales_contact_form(self,setup):
        self.log.info("-----------------Test-02------------------")
        self.driver = setup
        browser = Home_page_menu(self.driver)
        browser.open_home_page(self.url)
        browser.click_contact_sales_button(self.contact_sales)
        form = form_filling(self.driver)
        time.sleep(10)
        form.enter_name(self.name)
        form.enter_phone_number(self.phone_number)
        form.enter_email(self.email)
        form.enter_country(self.country)
        form.enter_no_of_employe(self.no_of_employe)
        form.job_title(self.job_title)
        form.your_message(self.your_message)
        time.sleep(30)
        form.submit(self.submite_button)
        form.test_verification_sales_contact()

    
    def test_03_positive_verificatio_of_demo_contact_form(self,setup):
        self.log.info("-----------------Test-03------------------")
        self.driver = setup
        browser = Home_page_menu(self.driver)
        browser.open_home_page(self.url)
        browser.click_booking_button(self.demo_booking)
        form = form_filling(self.driver)
        form.enter_name(self.name)
        form.enter_phone_number(self.phone_number)
        form.enter_email(self.email)
        form.enter_company(self.company)
        form.enter_country(self.country)
        form.enter_no_of_employe(self.no_of_employe)
        time.sleep(30)
        form.submit(self.submite_button)
        form.test_verification_demo_contact()

    def test_04_negative_verfication_of_sales_contact_form(self,setup):
        self.log.info("-----------------Test-04------------------")
        self.driver = setup
        browser = Home_page_menu(self.driver)
        browser.open_home_page(self.url)
        browser.click_contact_sales_button(self.contact_sales)
        form = form_filling(self.driver)
        form.enter_phone_number(self.phone_number)
        form.enter_email(self.email)
        form.enter_country(self.country)
        form.enter_no_of_employe(self.no_of_employe)
        form.job_title(self.job_title)
        form.your_message(self.your_message)
        time.sleep(30)
        form.submit(self.submite_button)
        form.test_negative_verification_sales_contact()

    def test_05_negative_verificatio_of_demo_contact_form(self,setup):
        self.log.info("-----------------Test-05------------------")
        self.driver = setup
        browser = Home_page_menu(self.driver)
        browser.open_home_page(self.url)
        browser.click_booking_button(self.demo_booking)
        form = form_filling(self.driver)
        form.enter_name(self.name)
        form.enter_phone_number(self.phone_number)
        form.enter_email(self.email)
        form.enter_company(self.company)
        form.enter_no_of_employe(self.no_of_employe)
        time.sleep(30)
        form.submit(self.submite_button)
        form.test_negative_verification_demo_contact()
        