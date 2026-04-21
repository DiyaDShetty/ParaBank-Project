from pages.login_page import LoginPage
from pages.transfer_funds_page import TransferFundsPage

def test_transfer_funds(driver):
    LoginPage(driver).login("john", "demo")

    transfer = TransferFundsPage(driver)
    transfer.transfer("50")

    assert transfer.transfer_success()
