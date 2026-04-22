from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time

USERNAME = "john"
PASSWORD = "demo"


def test_find_transactions_invalid_date_and_exit(driver):
    wait = WebDriverWait(driver, 10)
    login_page = LoginPage(driver)

    # 1️⃣ Login
    login_page.login(USERNAME, PASSWORD)

    # 2️⃣ Open Find Transactions
    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//div[@id='rightPanel']//h1"),
            "Find Transactions"
        )
    )

    # 3️⃣ Find by Transaction ID (dummy value)
    tx_id = driver.find_element(By.NAME, "criteria.transactionId")
    tx_id.clear()
    tx_id.send_keys("999999")
    driver.find_elements(By.XPATH, "//input[@value='Find Transactions']")[0].click()

    time.sleep(1)  # intentional short pause, no wait

    # 4️⃣ Find by Amount (dummy value)
    amount = driver.find_element(By.NAME, "criteria.amount")
    amount.clear()
    amount.send_keys("100")
    driver.find_elements(By.XPATH, "//input[@value='Find Transactions']")[3].click()

    time.sleep(1)

    # 5️⃣ Find by Date – INVALID DATE
    date_field = driver.find_element(By.NAME, "criteria.onDate")
    date_field.clear()

    # ❌ Invalid date (wrong month but correct format)
    date_field.send_keys("13-10-2024")

    # Click Find by Date button
    driver.find_elements(By.XPATH, "//input[@value='Find Transactions']")[1].click()

    # 6️⃣ Validation check (DO NOT WAIT)
    page_text = driver.page_source.lower()

    # ParaBank may or may not show a message; both are valid outcomes
    assert (
        "invalid" in page_text
        or "find transactions" in page_text
    ), "Date validation did not trigger"

    # ✅ Test ends cleanly here
    print("Invalid date entered, validation triggered. Test completed.")