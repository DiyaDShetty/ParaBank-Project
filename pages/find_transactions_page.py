from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

USERNAME = "john"
PASSWORD = "demo"


def test_find_transactions_invalid_date_only(driver):
    wait = WebDriverWait(driver, 10)
    login_page = LoginPage(driver)

    # 1️⃣ Login
    login_page.login(USERNAME, PASSWORD)

    # 2️⃣ Navigate to Find Transactions
    driver.find_element(By.LINK_TEXT, "Find Transactions").click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//div[@id='rightPanel']//h1"),
            "Find Transactions"
        )
    )

    # 3️⃣ Enter INVALID date (wrong month, valid format)
    date_field = wait.until(
        EC.presence_of_element_located((By.ID, "transactionDate"))
    )
    date_field.clear()
    date_field.send_keys("demo")  # ❌ invalid month

    # 4️⃣ Click Find by Date
    driver.find_element(By.ID, "findByDate").click()

    # 5️⃣ Validate error message is shown
    error_message = wait.until(
        EC.visibility_of_element_located((By.ID, "transactionDateError"))
    ).text

    assert error_message != "", "Expected validation error message was not shown"

    print("Invalid date validation triggered successfully.")
