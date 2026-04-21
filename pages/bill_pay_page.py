from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BillPayPage(BasePage):

    def pay_bill(self):
        self.click((By.LINK_TEXT, "Bill Pay"))
        self.type((By.NAME, "payee.name"), "Electricity Board")
        self.type((By.NAME, "payee.address.street"), "MG Road")
        self.type((By.NAME, "payee.address.city"), "Bangalore")
        self.type((By.NAME, "payee.address.state"), "KA")
        self.type((By.NAME, "payee.address.zipCode"), "560001")
        self.type((By.NAME, "payee.phoneNumber"), "9876543210")
        self.type((By.NAME, "payee.accountNumber"), "12345")
        self.type((By.NAME, "verifyAccount"), "12345")
        self.type((By.NAME, "amount"), "20")
        self.click((By.XPATH, "//input[@value='Send Payment']"))

    def bill_paid(self):
        return "Bill Payment Complete" in self.driver.page_source
