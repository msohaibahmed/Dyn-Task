import pytest
from config.settings import Config
from pages.login_page import LoginPage
from pages.registration_page import InitialRegistrationPage, RegistrationDetailsPage 
import time
from utilities import helper
from faker import Faker

@pytest.mark.registration
def test_user_registration_without_subscription(driver):
    initial_registration_page = InitialRegistrationPage(driver=driver)
    initial_registration_page.load()
    helper.handle_cookies_modal(driver=driver)
    initial_registration_page.start_registration()
    time.sleep(1)

    registration_data_page = RegistrationDetailsPage(driver=driver)
    assert driver.current_url == registration_data_page.url, "Unable to load Registration data page."

    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_email = fake.email()
    repeat_user_email = user_email
    user_password = helper.generate_password()

    registration_data_page.enter_details(fname=first_name, lname=last_name, user_email=user_email, repeat_user_email=repeat_user_email, user_password=user_password)
    registration_data_page.submit_registration()
    registration_errors = registration_data_page.get_errors_on_page()
    assert len(registration_errors) == 0 , f"There are some errors on registration {registration_errors}"
    time.sleep(5)
    assert "bezahlen" in driver.current_url, "Unable to load payment page." 
    driver = helper.restart_browser(driver=driver)
    login_page = LoginPage(driver=driver, login_url=Config.BASE_URL + "/anmelden")
    login_page.go_to_login_page()
    time.sleep(1)
    login_page.login(user_email, user_password)
    time.sleep(5)
    assert driver.current_url == "https://www.dyn.sport/resubscribe", "Unable to register new user."
