import sys
import os
import time
from selenium import webdriver

# ✅ Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.open_account_login_page import LoginPage
from pages.open_account_page import OpenAccountPage


def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    return driver


def test_open_savings_account():
    driver = setup_driver()

    try:
        # Login
        login = LoginPage(driver)
        login.login("john", "demo")

        time.sleep(2)

        # Open Account
        account = OpenAccountPage(driver)
        account.navigate_to_open_account()

        time.sleep(2)

        account.open_savings_account()

        time.sleep(2)

        result = account.verify_account_created()

        print("Result:", result)

        assert "Account Opened!" in result

    finally:
        time.sleep(2)
        driver.quit()