from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")
