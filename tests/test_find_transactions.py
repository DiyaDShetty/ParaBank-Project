from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FindTransactionsPage(BasePage):

    def open_find_transactions(self):
        self.click((By.LINK_TEXT, "Find Transactions"))

    def find_by_transaction_id(self, txn_id):
        self.type((By.ID, "criteria.transactionId"), txn_id)
        self.click((By.XPATH, "//button[contains(text(),'Find')]"))

    def results_displayed(self):
        return "Transaction Results" in self.driver.page_source
