from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FindTransactionsPage(BasePage):

    def find_by_amount(self, amount="20"):
        self.click((By.LINK_TEXT, "Find Transactions"))
        self.type((By.ID, "criteria.amount"), amount)
        self.click((By.XPATH, "//button[contains(text(),'Find')]"))

    def results_displayed(self):
        return "Transaction Results" in self.driver.page_source
