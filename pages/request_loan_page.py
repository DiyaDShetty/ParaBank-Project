from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RequestLoanPage(BasePage):

    def request_loan(self):
        self.click((By.LINK_TEXT, "Request Loan"))
        self.type((By.ID, "amount"), "1000")
        self.type((By.ID, "downPayment"), "100")
        self.click((By.XPATH, "//input[@value='Apply Now']"))

    def loan_processed(self):
        return "Loan Request Processed" in self.driver.page_source