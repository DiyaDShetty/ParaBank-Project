from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpenAccountPage(BasePage):

    def open_new_account(self):
        self.click((By.LINK_TEXT, "Open New Account"))
        self.click((By.XPATH, "//input[@value='Open New Account']"))

    def account_opened(self):
        return "Account Opened!" in self.driver.page_source