import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Start browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://parabank.parasoft.com")

wait = WebDriverWait(driver, 20)

try:
    # Step 2: Click on Register link
    register_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
    )
    register_link.click()

    # Step 3: Fill registration form
    wait.until(EC.visibility_of_element_located((By.ID, "customer.firstName")))

    driver.find_element(By.ID, "customer.firstName").send_keys("Diya")
    driver.find_element(By.ID, "customer.lastName").send_keys("Shetty")
    driver.find_element(By.ID, "customer.address.street").send_keys("123 Main Street")
    driver.find_element(By.ID, "customer.address.city").send_keys("Bangalore")
    driver.find_element(By.ID, "customer.address.state").send_keys("Karnataka")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("560001")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID, "customer.ssn").send_keys("123456789")

    # username & password
    driver.find_element(By.ID, "customer.username").send_keys("diyashett")
    driver.find_element(By.ID, "customer.password").send_keys("Test@123")
    driver.find_element(By.ID, "repeatedPassword").send_keys("Test@123")

    # Step 4: Click Register button
    driver.find_element(By.XPATH, "//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input").click()

    # Step 5: Validate success
    success_msg = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='rightPanel']/h1"))
    )
    print("Registration successful!")

finally:
    # Step 6: Close browser
    time.sleep(100)
    driver.quit()
