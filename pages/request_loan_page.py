from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RequestLoanPage(BasePage):

    REQUEST_LOAN_LINK = (By.LINK_TEXT, "Request Loan")
    APPLY_NOW_BUTTON = (By.XPATH, "//input[@value='Apply Now']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")  # ParaBank shows error text

    def go_to_request_loan(self):
        self.click(self.REQUEST_LOAN_LINK)

    def submit_loan_with_empty_fields(self):
        # Do NOT enter amount or down payment
        self.click(self.APPLY_NOW_BUTTON)

    def loan_request_failed(self):
        return "error" in self.driver.page_source.lower()
