from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class FindTransactionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.find_transactions_link = (By.LINK_TEXT, "Find Transactions")
        self.account_dropdown = (By.ID, "accountId")   # important
        self.date_field = (By.ID, "transactionDate")
        self.find_btn = (By.ID, "findByDate")

    def navigate_to_find_transactions(self):
        self.wait.until(EC.element_to_be_clickable(self.find_transactions_link)).click()

    def select_account(self, account_number):
        dropdown_element = self.wait.until(
            EC.presence_of_element_located(self.account_dropdown)
        )
        select = Select(dropdown_element)
        select.select_by_visible_text(account_number)

    def search_by_date(self, date):
        date_input = self.wait.until(EC.presence_of_element_located(self.date_field))
        date_input.clear()
        date_input.send_keys(date)

        self.wait.until(EC.element_to_be_clickable(self.find_btn)).click()

    def search_today_date(self):
        today_date = datetime.today().strftime("%m-%d-%Y")  # MM-DD-YYYY

        date_input = self.wait.until(
            EC.presence_of_element_located(self.date_field)
        )
        date_input.clear()
        date_input.send_keys(today_date)

        self.wait.until(EC.element_to_be_clickable(self.find_btn)).click()