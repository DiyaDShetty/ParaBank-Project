import pytest

from pages.registration_page import RegistrationPage
import time

@pytest.mark.order(1)
def test_parabank_registration(driver):
    registration = RegistrationPage(driver)

    registration.go_to_registration()
    registration.fill_registration_form()
    registration.submit()

    assert registration.is_registration_successful()