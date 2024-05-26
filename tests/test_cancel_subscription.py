from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.peofile_subscription_page import ProfileSubscriptionPage
from config.settings import Config
import time
import pytest

@pytest.mark.cancel
def test_cancel_subscription(driver):
    login_page = LoginPage(driver=driver, login_url=Config.BASE_URL + "/anmelden")
    login_page.go_to_login_page()
    time.sleep(1)
    login_page.login("marvin.klaproth+freetrial+monthly@dynmedia.com", "DynSportTest102!")
    time.sleep(1)
    # Assertions to verify successful login can go here
    assert driver.current_url == "https://www.dyn.sport/", "Unable to login."

    profile_page = ProfilePage(driver=driver)
    profile_page.load()
    time.sleep(1)
    profile_page.open_my_subscription_page()
    time.sleep(5)
    profile_subscription_page = ProfileSubscriptionPage(driver=driver)
    assert driver.current_url == profile_subscription_page.url, "Unable to load profile page"

    profile_subscription_page.cancel_subscription()
    time.sleep(1)
    profile_subscription_page.select_cancellation_reason()
    time.sleep(1)
    profile_subscription_page.confirm_cancel_subscription()
    time.sleep(5)
    profile_subscription_page.confirm_cancel_subscriotion_final_step()
    time.sleep(5)
    cancel_confirmation = profile_subscription_page.get_confirmation_cancel_subs_element()
    time.sleep(5)
    assert cancel_confirmation.text == "Erfolgreich gekündigt", "Unable to cancel subscription."
