from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//input[@value='Log In']")
        self.error_msg = (By.XPATH, "//h1[@class='title']")

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.username)).clear()
        self.driver.find_element(*self.username).send_keys(username)

        self.wait.until(EC.presence_of_element_located(self.password)).clear()
        self.driver.find_element(*self.password).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def get_error_title(self):
        return self.wait.until(
            EC.presence_of_element_located(self.error_msg)
        ).text