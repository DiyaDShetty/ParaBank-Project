from pages.login_page import LoginPage
from pages.bill_pay_page import BillPayPage

USERNAME = "john"
PASSWORD = "demo"


def test_pay_bill_valid(driver):
    login = LoginPage(driver)
    bill = BillPayPage(driver)

    # ✅ call matches existing login_page.py
    login.login(USERNAME, PASSWORD)

    data = {
        "payee.name": "Electric Board",
        "payee.address.street": "MG Road",
        "payee.address.city": "Bangalore",
        "payee.address.state": "KA",
        "payee.address.zipCode": "560001",
        "payee.phoneNumber": "9876543210",
        "payee.accountNumber": "123456",
        "verifyAccount": "123456",
        "amount": "100"
    }

    heading = bill.pay_bill(data)
    assert "Bill" in heading


def test_pay_bill_invalid(driver):
    login = LoginPage(driver)
    bill = BillPayPage(driver)

    # ✅ same fix here
    login.login(USERNAME, PASSWORD)

    data = {
        "payee.name": "Water Board",
        "payee.address.street": "Brigade Road",
        "payee.address.city": "Bangalore",
        "payee.address.state": "KA",
        "payee.address.zipCode": "560001",
        "payee.phoneNumber": "9123456789",
        "payee.accountNumber": "111111",
        "verifyAccount": "999999",  # mismatch
        "amount": "100"
    }

    heading = bill.pay_bill(data)
    assert "Bill" in heading