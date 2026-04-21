from pages.login_page import LoginPage
from pages.bill_pay_page import BillPayPage

def test_bill_payment(driver):
    LoginPage(driver).login("john", "demo")

    bill_pay = BillPayPage(driver)
    bill_pay.pay_bill()

    assert bill_pay.bill_paid()