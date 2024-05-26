from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfileSubscriptionPage:
    cancel_subscription_btn = (By.ID, "profileSubscriptionManageCancelCta")
    quit_modal_form = (By.ID, "profileSubscriptionManageTerminateQuestionModalForm")
    reason_radio_btn = (By.CSS_SELECTOR, "label.group:nth-of-type(2)>span:nth-of-type(2)")
    confirm_cancel_subscription_btn = (By.ID, "profileSubscriptionCancelQuestionModalFormCta")
    confirm_cancel_subs_modal_btn = (By.ID, "profileSubscriptionCancelModalCta")
    revoke_cancel_subs_btn = (By.CSS_SELECTOR, '[data-testid="profile-subscription-cancel-revoke-cancellation--button"]')

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://profil.dyn.sport/abo"

    def load(self):
        self.driver.get(self.url)

    def cancel_subscription(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cancel_subscription_btn)
        ).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.quit_modal_form))

    
    def select_cancellation_reason(self):
        radio_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.reason_radio_btn) and EC.visibility_of_element_located(self.reason_radio_btn)
        )
        radio_btn.click()
    
    def confirm_cancel_subscription(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_cancel_subscription_btn)
        ).click()
    
    def confirm_cancel_subscriotion_final_step(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_cancel_subs_modal_btn)
        ).click()

    def get_confirmation_cancel_subs_element(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Erfolgreich gekündigt")]')))
        return element
    
    def revoke_cancellation(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.revoke_cancel_subs_btn))
        element.click()
    
    def get_user_active_status(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Aktiv")]')))
        return element