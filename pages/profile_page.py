from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    my_account_btn = (By.XPATH, '//a[@href="/"]')
    my_subscription_btn = (By.XPATH, '//a[@href="/abo"]')
    move_sport_btn = (By.XPATH, '//a[@href="/move-your-sport"]')
    sport_profile_btn = (By.XPATH, '//a[@href="//sportprofil"]')

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://profil.dyn.sport/"

    def load(self):
        self.driver.get(self.url)

    def open_my_account(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.my_account_btn)
        ).click()
    
    def open_my_subscription_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.my_subscription_btn)
        ).click()

    