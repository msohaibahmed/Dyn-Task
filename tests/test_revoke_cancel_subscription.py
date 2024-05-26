from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.peofile_subscription_page import ProfileSubscriptionPage
from config.settings import Config
import time
import pytest
from utilities import helper

def test_revoke_cancel_subscription(driver):
    login_page = LoginPage(driver=driver, login_url=Config.BASE_URL + "/anmelden")
    login_page.go_to_login_page()
    time.sleep(10)
    login_page.login("marvin.klaproth+freetrial+monthly@dynmedia.com", "DynSportTest102!")
    time.sleep(5)
    # Assertions to verify successful login can go here
    assert driver.current_url == "https://www.dyn.sport/", "Unable to login."

    profile_page = ProfilePage(driver=driver)
    profile_page.load()
    time.sleep(1)
    profile_page.open_my_subscription_page()
    time.sleep(10)
    profile_subscription_page = ProfileSubscriptionPage(driver=driver)
    assert driver.current_url == profile_subscription_page.url, "Unable to load profile page"

    time.sleep(5)
    profile_subscription_page.revoke_cancellation()
    time.sleep(5)
    assert profile_subscription_page.get_user_active_status().text == "Aktiv", "Unable to revoke cancellation"