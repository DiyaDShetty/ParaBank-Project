from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.logout import logout
from pages.overview import login
def test_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    wait = WebDriverWait(driver, 10)
    login(wait)
    Result=logout(wait)
    assert "Customer Login" in Result,"logout failed"
    driver.quit()