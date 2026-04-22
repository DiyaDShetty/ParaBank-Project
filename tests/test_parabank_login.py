import pytest

from pages.login_page import LoginPage

@pytest.mark.order(2)
def test_parabank_login(driver):
    login = LoginPage(driver)
    login.login("john", "demo")

    assert login.login_successful()
