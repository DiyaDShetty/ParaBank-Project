from pages.transfer_funds import transfer_funds
from pages.overview import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


def test_parabank_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    wait = WebDriverWait(driver, 10)
    login(wait)
    wait = WebDriverWait(driver, 10)
    success_text = transfer_funds(wait)
    assert "Transfer Complete" in success_text
    print("transfer complete passed")