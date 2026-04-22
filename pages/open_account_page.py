from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class OpenAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.open_account_link = (By.LINK_TEXT, "Open New Account")
        self.account_type_dropdown = (By.ID, "type")
        self.from_account_dropdown = (By.ID, "fromAccountId")
        self.open_account_btn = (By.XPATH, "//input[@value='Open New Account']")
        self.success_msg = (By.XPATH, "//h1[contains(text(),'Account Opened!')]")

    def navigate_to_open_account(self):
        self.wait.until(
            EC.element_to_be_clickable(self.open_account_link)
        ).click()

    def open_savings_account(self):
        # Select SAVINGS
        dropdown = self.wait.until(
            EC.presence_of_element_located(self.account_type_dropdown)
        )
        Select(dropdown).select_by_visible_text("SAVINGS")

        # Select first available account
        from_account = self.wait.until(
            EC.presence_of_element_located(self.from_account_dropdown)
        )
        Select(from_account).select_by_index(0)

        # Click Open Account
        button = self.wait.until(
            EC.presence_of_element_located(self.open_account_btn)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def verify_account_created(self):
        return self.wait.until(
            EC.presence_of_element_located(self.success_msg)
        ).text