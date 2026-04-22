from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def logout(wait):
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Log Out"))).click()
    logout=wait.until(EC.visibility_of_element_located((By.XPATH, "//h2"))).text
    return logout
