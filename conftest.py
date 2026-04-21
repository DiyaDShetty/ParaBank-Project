import pytest
import os
from selenium import webdriver
from datetime import datetime

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            filename = f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(filename)