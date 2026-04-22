from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.overview import login,account_overview, account_details

# Account Overview Assertion
def test_parabank_overview():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    wait = WebDriverWait(driver, 10)
    login(wait)
    overview_text = account_overview(wait)
    assert "Accounts Overview" in overview_text
    print(" account overview passed")
    # Account Details Assertion
    details_text = account_details(wait)
    assert "Account Details" in details_text
    print(" account details passed")
    driver.quit()