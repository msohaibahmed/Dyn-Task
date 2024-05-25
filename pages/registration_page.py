from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InitialRegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://konto.dyn.sport/registrieren"

    def load(self):
        self.driver.get(self.url)

    def start_registration(self):
        start_button = (By.ID, "start_registration")  # Replace 'start_registration' with the actual ID of the button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(start_button)
        ).click()


class RegistrationDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://konto.dyn.sport/registrieren/daten"

    def enter_details(self, email, password):
        email_input = (By.ID, "email")  # Replace 'email' with the actual ID
        password_input = (By.ID, "password")  # Replace 'password' with the actual ID

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(email_input)
        ).send_keys(email)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(password_input)
        ).send_keys(password)

    def submit_registration(self):
        submit_button = (By.ID, "submit_registration")  # Replace 'submit_registration' with the actual ID
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(submit_button)
        ).click()
