from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UpdateContactPage(BasePage):

    UPDATE_CONTACT_LINK = (By.LINK_TEXT, "Update Contact Info")
    PHONE_FIELD = (By.ID, "customer.phoneNumber")
    UPDATE_BUTTON = (By.XPATH, "//input[@value='Update Profile']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")

    def go_to_update_contact(self):
        self.click(self.UPDATE_CONTACT_LINK)

    def update_with_invalid_phone(self):
        # Enter invalid phone number (alphabets instead of digits)
        self.type(self.PHONE_FIELD, "abcde123")
        self.click(self.UPDATE_BUTTON)

    def update_failed(self):
        return "error" in self.driver.page_source.lower()