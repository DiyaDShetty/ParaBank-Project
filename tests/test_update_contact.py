from pages.login_page import LoginPage
from pages.update_contact_page import UpdateContactPage

def test_update_contact_info(driver):
    LoginPage(driver).login("john", "demo")

    update_contact = UpdateContactPage(driver)
    update_contact.update_contact()

    assert update_contact.update_success()