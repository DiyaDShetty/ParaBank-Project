from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage

def test_open_new_account(driver):
    LoginPage(driver).login("john", "demo1")

    open_account = OpenAccountPage(driver)
    open_account.open_new_account()

    assert open_account.account_opened()
