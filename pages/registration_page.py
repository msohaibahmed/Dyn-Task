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
        start_button = (By.ID, "abowahlCta")  # Replace 'start_registration' with the actual ID of the button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(start_button)
        ).click()


class RegistrationDetailsPage:

    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "email")
    repeat_email = (By.ID, "emailRepeat")        
    password = (By.ID, "password")
    privacy_check_box = (By.CSS_SELECTOR, ".relative:nth-child(3) div:nth-child(2) span:nth-of-type(1)")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://konto.dyn.sport/registrieren/daten"

    def enter_details(self, fname, lname, user_email, repeat_user_email, user_password):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(fname)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(lname)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(user_email)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.repeat_email)
        ).send_keys(repeat_user_email)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(user_password)

        check_box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.privacy_check_box)
        )
        check_box.click()


    def submit_registration(self):
        submit_button = (By.ID, "registrationFormCta")  # Replace 'submit_registration' with the actual ID
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(submit_button)
        ).click()

    def get_errors_on_page(self):
        errors = []
        error_fields = {
            "firstName": "First name required",
            "lastName": "Last name required",
            "email": "Email required",
            "emailRepeat": "Repeat email is required",
            "password": "Password is required",
        }

        for field_id, error_message in error_fields.items():
            element = self.driver.find_element(By.ID, field_id)
            if "red" in element.get_attribute("class"):
                errors.append(error_message)

        return errors
        


