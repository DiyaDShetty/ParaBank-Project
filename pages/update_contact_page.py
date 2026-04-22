from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpdateContactInfoPage:
    UPDATE_CONTACT_LINK = (By.LINK_TEXT, "Update Contact Info")

    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    STREET = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIPCODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")

    UPDATE_BUTTON = (By.XPATH, "//input[@value='Update Profile']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']//p")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_update_contact_info(self):
        self.driver.find_element(*self.UPDATE_CONTACT_LINK).click()

    def update_contact_info(self, first, last, street, city, state, zip_code, phone):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)

        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(last)

        self.driver.find_element(*self.STREET).clear()
        self.driver.find_element(*self.STREET).send_keys(street)

        self.driver.find_element(*self.CITY).clear()
        self.driver.find_element(*self.CITY).send_keys(city)

        self.driver.find_element(*self.STATE).clear()
        self.driver.find_element(*self.STATE).send_keys(state)

        self.driver.find_element(*self.ZIPCODE).clear()
        self.driver.find_element(*self.ZIPCODE).send_keys(zip_code)

        self.driver.find_element(*self.PHONE).clear()
        self.driver.find_element(*self.PHONE).send_keys(phone)

        self.driver.find_element(*self.UPDATE_BUTTON).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text
