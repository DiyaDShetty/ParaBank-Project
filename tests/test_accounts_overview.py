from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage

def test_accounts_overview(driver):
    LoginPage(driver).login("john", "demo")

    accounts = AccountsPage(driver)
    assert accounts.accounts_loaded()
