from pages.login_page import LoginPage
from pages.update_contact_page import UpdateContactInfoPage

USERNAME = "john"
PASSWORD = "demo"


def test_update_contact_info_valid(driver):
    login_page = LoginPage(driver)
    update_page = UpdateContactInfoPage(driver)

    # ✅ Login
    login_page.login(USERNAME, PASSWORD)

    # ✅ Navigate to Update Contact Info
    update_page.open_update_contact_info()

    # ✅ Update with valid information
    update_page.update_contact_info(
        first="John",
        last="Doe",
        street="MG Road",
        city="Bangalore",
        state="KA",
        zip_code="560001",
        phone="9876543210"
    )

    # ✅ Verify success message
    success_message = update_page.get_success_message()
    assert "updated" in success_message.lower()