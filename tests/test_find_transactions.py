import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.find_transaction_login_page import LoginPage
import pages.find_transactions_page
from pages.find_transactions_by_date_page import FindTransactionsPage


def setup_driver():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    return driver


def test_find_transaction():
    driver = setup_driver()

    try:
        # Login
        login = LoginPage(driver)
        # login.login("tomsmith", "SuperSecretPassword!")
        login.login("john", "demo")

        time.sleep(2)

        # Navigate and search
        find_txn = FindTransactionsPage(driver)
        find_txn.navigate_to_find_transactions()
        find_txn.select_account("13344")
        find_txn.search_today_date()

        time.sleep(2)

        # Validation
        assert driver.find_element(By.TAG_NAME, "body").text.__contains__("Transaction Results")

    finally:
        time.sleep(2)
        driver.quit()