import pytest
from utilities.driver_factory import DriverFactory
from config.settings import Config

@pytest.fixture(scope="session")
def config():
    return Config()

@pytest.fixture(scope="session")
def driver(config):
    driver = DriverFactory.get_driver(config.BROWSER)
    yield driver
    driver.quit()
