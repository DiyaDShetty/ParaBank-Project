from pages.login_page import LoginPage
from pages.request_loan_page import RequestLoanPage

def test_request_loan(driver):
    LoginPage(driver).login("john", "demo")

    loan = RequestLoanPage(driver)
    loan.request_loan()

    assert loan.loan_processed()
