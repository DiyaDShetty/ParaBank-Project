from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TransferFundsPage:
    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT = (By.ID, "amount")
    TRANSFER_BTN = (By.XPATH, "//input[@value='Transfer']")
    HEADING = (By.XPATH, "//div[@id='rightPanel']//h1")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def transfer_money(self, amount):
        self.driver.find_element(*self.TRANSFER_LINK).click()
        self.wait.until(EC.visibility_of_element_located(self.AMOUNT)).send_keys(amount)
        self.driver.find_element(*self.TRANSFER_BTN).click()
        return self.wait.until(EC.visibility_of_element_located(self.HEADING)).text