from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TransferFundsPage(BasePage):

    def transfer(self, amount="50"):
        self.click((By.LINK_TEXT, "Transfer Funds"))
        self.type((By.ID, "amount"), amount)
        self.click((By.XPATH, "//input[@value='Transfer']"))

    def transfer_success(self):
        return "Transfer Complete!" in self.driver.page_source
