from pages.Search import Search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.overview import login

def test_searchamount():
    # Account Overview Assertion
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    wait = WebDriverWait(driver, 10)
    login(wait)
    wait = WebDriverWait(driver, 10)
    Search_result=Search(wait)
    assert "Transaction Results" in Search_result,"search assertion failed"
    print("Search assertion passed")
    driver.quit()