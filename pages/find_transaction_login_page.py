from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//input[@value='Log In']")

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()