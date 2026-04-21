from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountsPage(BasePage):

    def accounts_loaded(self):
        return "Accounts Overview" in self.driver.page_source

    def logout(self):
        self.click((By.LINK_TEXT, "Log Out"))

    def logged_out(self):
        return "Customer Login" in self.driver.page_source
