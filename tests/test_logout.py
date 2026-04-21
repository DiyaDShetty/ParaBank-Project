from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage

def test_logout(driver):
    LoginPage(driver).login("john", "demo")

    accounts = AccountsPage(driver)
    accounts.logout()

    assert accounts.logged_out()
