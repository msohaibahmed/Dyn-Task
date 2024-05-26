import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

def generate_password():
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:',.<>/?`~"  # Define any special characters you want included

    # Ensure at least one character from each set is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length to ensure it is at least 12 characters
    remaining_length = max(12, len(password)) - len(password)
    remaining_chars = random.choices(lower + upper + digits + special, k=remaining_length)

    # Combine all characters and shuffle them to avoid predictable patterns
    password += remaining_chars
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

def restart_browser(driver):
    """Closes the current browser and starts a new one."""
    driver.quit()  # Close the current browser session
    driver = webdriver.Chrome()  # Start a new browser session
    return driver

def handle_cookies_modal(driver):
        try:
            import time
            time.sleep(10)
            element = driver.execute_script('return document.querySelector("#usercentrics-root").shadowRoot.querySelector("#uc-center-container")')
            element.find_element(By.CSS_SELECTOR, '[data-testid="uc-accept-all-button"]').click()
        except TimeoutException as te:
            print(f"Cookie modal did not appear or took too long.{te}")