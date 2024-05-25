from pages.login_page import LoginPage
from config.settings import Config
import time

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to(Config.BASE_URL + "/anmelden")
    login_page.enter_username("marvin.klaproth+freetrial+monthly@dynmedia.com")
    login_page.enter_password("DynSportTest102!")
    time.sleep(20)
    login_page.click_login()
    print(driver.current_url)

    # Assertions to verify successful login can go here
    assert driver.current_url == "https://profil.dyn.sport/"
