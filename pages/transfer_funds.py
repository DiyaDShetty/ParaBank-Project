from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def transfer_funds(wait):
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Transfer"))).click()

    wait.until(EC.visibility_of_element_located((By.NAME, "input"))).send_keys("89")

    from_dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, "fromAccountId"))))
    wait.until(lambda driver: len(from_dropdown.options) > 0)

    first_value = from_dropdown.options[0].get_attribute("value")
    from_dropdown.select_by_value(first_value)

    to_dropdown = Select(wait.until(EC.visibility_of_element_located((By.ID, "toAccountId"))))
    to_value = to_dropdown.options[0].get_attribute("value")
    to_dropdown.select_by_value(to_value)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Transfer']"))).click()

    success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "(//h1)[2]"))).text
    return success_msg