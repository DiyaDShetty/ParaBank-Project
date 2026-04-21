from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def login(self, user, pwd):
        self.type((By.NAME, "username"), user)
        self.type((By.NAME, "password"), pwd)
        self.click((By.XPATH, "//input[@value='Log In']"))

    def login_successful(self):
        return "Accounts Overview" in self.driver.page_source