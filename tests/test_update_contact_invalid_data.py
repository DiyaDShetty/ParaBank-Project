from pages.login_page import LoginPage
from pages.update_contact_page import UpdateContactPage

def test_update_contact_with_invalid_data(driver):
    # Login first
    LoginPage(driver).login("john", "demo")

    update_contact = UpdateContactPage(driver)
    update_contact.go_to_update_contact()
    update_contact.update_with_invalid_phone()

    assert update_contact.update_failed()