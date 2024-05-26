from pages.login_page import LoginPage
from config.settings import Config
import time
import pytest

@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver=driver, login_url=Config.BASE_URL + "/anmelden")
    login_page.go_to_login_page()
    time.sleep(1)
    login_page.login("marvin.klaproth+freetrial+monthly@dynmedia.com", "DynSportTest102!")
    time.sleep(1)
    assert driver.current_url == "https://www.dyn.sport/"
