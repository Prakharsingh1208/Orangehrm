import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\pranj\OneDrive\Desktop\orangehrm\configuration\config.ini")

class ReadConfig_menu:
    def get_application_url():
        url = config.get("Homepage - menu", "url")
        return url
    def get_booking_button():
        booking = config.get("Homepage - menu","Book_demo_button_xpath")
        return booking
    def get_contact_sales_button():
        contact = config.get("Homepage - menu","contact_sales_button_xpath")
        return contact
    def get_cross_button():
        cross = config.get("Homepage - menu","cross_button_xpath")
        return cross

class ReadConfig_contact_form:
    def get_name():
        name = config.get("sale/demo - contactform","full_name_xpath")
        return name
    def get_phone_number():
        phone_number = config.get("sale/demo - contactform","phone_number_xpath")
        return phone_number
    def get_email():
        email = config.get("sale/demo - contactform","email_xpath")
        return email
    def get_company_name():
        company_name = config.get("sale/demo - contactform","company_name_xpath")
        return company_name
    def get_country():
        country = config.get("sale/demo - contactform","country_xpath")
        return country
    def get_number_of_employes():
        employ_number = config.get("sale/demo - contactform","number_of_employes_xpath")
        return employ_number
    
    def get_contact_sales():
        button = config.get("sale/demo - contactform", "contact_sales_id")
        return button
    
    def get_your_message():
        your_message = config.get("sale/demo - contactform","your_message_xpath")
        return your_message

    def get_job_title():
        job_title = config.get("sale/demo - contactform","job_title_xpath")
        return job_title