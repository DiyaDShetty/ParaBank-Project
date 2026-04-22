from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def Search(wait):
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Find Transactions"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "amount"))).send_keys("89")
    wait.until(EC.presence_of_element_located((By.ID, "findByAmount"))).click()
    Result=wait.until(EC.visibility_of_element_located((By.XPATH, "(//h1)[2]"))).text
    return Result