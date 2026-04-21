from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UpdateContactPage(BasePage):

    def update_contact(self):
        self.click((By.LINK_TEXT, "Update Contact Info"))
        self.type((By.ID, "customer.phoneNumber"), "9999999999")
        self.click((By.XPATH, "//input[@value='Update Profile']"))

    def update_success(self):
        return "Profile Updated" in self.driver.page_source
