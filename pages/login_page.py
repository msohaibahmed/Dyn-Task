from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver, login_url):
        self.driver = driver
        self.login_url = login_url
        self.username_locator = (By.ID, "email")
        self.password_locator = (By.ID, "password")
        self.submit_button_locator = (By.ID, "loginFormCta")
        self.cookie_accept_locator = (By.CSS_SELECTOR, 'button[data-testid="uc-accept-all-button"]')
        self.cookie_modal_locator = (By.CSS_SELECTOR, '[data-testid="uc-tcf-first-layer"]')

    def go_to_login_page(self):
        self.driver.get(self.login_url)
        self.handle_cookies_modal()

    def handle_cookies_modal(self):
        # await page.waitForSelector('button[data-testid="uc-accept-all-button"]', { timeout: 5000 });
        try:
            # WebDriverWait(self.driver, 50).until(
            #     EC.visibility_of_element_located(self.cookie_modal_locator)
            # )
            accept_button = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable(self.cookie_accept_locator)
            )
            accept_button.click()
            # WebDriverWait(self.driver, 20).until(
            #     EC.invisibility_of_element_located(self.cookie_modal_locator)
            # )
            print("Cookies have been accepted.")
        except TimeoutException as te:
            print(f"Cookie modal did not appear or took too long.{te}")

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_locator)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_locator)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_submit_button(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.submit_button_locator)
            )
            submit_button.click()
            WebDriverWait(self.driver, 10)
        except Exception as e:
            print(f"Failed to click on the submit button due to: {e}")
            # self.force_click(self.submit_button_locator)

    def force_click(self, by_locator):
        # Using JavaScript to perform the click if normal click fails
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator)
        )
        try:
            self.driver.execute_script("arguments[0].click();", element)
            print("Clicked using JavaScript.")
        except Exception as e:
            print(f"JavaScript click failed: {e}")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()
