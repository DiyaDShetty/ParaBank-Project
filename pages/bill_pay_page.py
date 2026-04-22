from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BillPayPage:
    BILL_PAY = (By.LINK_TEXT, "Bill Pay")
    HEADING = (By.XPATH, "//div[@id='rightPanel']//h1")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def pay_bill(self, data):
        self.driver.find_element(*self.BILL_PAY).click()

        for field, value in data.items():
            self.driver.find_element(By.NAME, field).send_keys(value)

        self.driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()
        return self.wait.until(EC.visibility_of_element_located(self.HEADING)).text