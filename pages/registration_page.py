from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):

    REGISTER_LINK = (By.LINK_TEXT, "Register")

    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")

    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Welcome')]")

    def go_to_registration(self):
        self.click(self.REGISTER_LINK)

    def fill_registration_form(self):
        self.type(self.FIRST_NAME, "Diya")
        self.type(self.LAST_NAME, "Shetty")
        self.type(self.ADDRESS, "123 Main Street")
        self.type(self.CITY, "Bangalore")
        self.type(self.STATE, "Karnataka")
        self.type(self.ZIP, "560001")
        self.type(self.PHONE, "9876543210")
        self.type(self.SSN, "123456789")

        # Deliberate reuse to demonstrate failure/validation behavior
        self.type(self.USERNAME, "diyashetty_01")
        self.type(self.PASSWORD, "Test@123")
        self.type(self.CONFIRM_PASSWORD, "Test@123")

    def submit(self):
        self.click(self.REGISTER_BUTTON)

    def is_registration_successful(self):
        message = self.wait.until(
            lambda d: d.find_element(*self.SUCCESS_MESSAGE)
        )
        return "Welcome" in message.text