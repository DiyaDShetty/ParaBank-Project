from pages.login_page import LoginPage
from pages.request_loan_page import RequestLoanPage

def test_request_loan_with_empty_fields(driver):
    # Login first
    LoginPage(driver).login("john", "demo")

    loan = RequestLoanPage(driver)
    loan.go_to_request_loan()
    loan.submit_loan_with_empty_fields()

    assert loan.loan_request_failed()
