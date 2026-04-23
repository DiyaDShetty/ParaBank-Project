from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

def login(wait):
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("john")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("demo")
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input)[3]"))).click()

def account_overview(wait):
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Accounts Overview"))).click()
    account_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1"))).text
    wait.until(EC.element_to_be_clickable((By.XPATH, "//table//a"))).click()
    return account_page


def account_details(wait):
    account_page = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
    return account_page



# def transactions(wait, driver):
#     month_dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, "month"))))
#     month_dropdown.select_by_value("April")
#
#     wait.until(EC.element_to_be_clickable((By.XPATH, "(//input)[1]"))).click()
#
#     wait.until(EC.element_to_be_clickable((By.XPATH, "(//a)[19]"))).click()
#
#     driver.back()
#     driver.back()





