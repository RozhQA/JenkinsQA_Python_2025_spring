import pytest

from core.settings import Config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker


@pytest.fixture(scope="session")
def config():
    return Config.load()


@pytest.fixture(scope="function")
def driver(config):

    match config.browser.NAME:
        case "chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_CHROME.split(';'):
                options.add_argument(argument)
            driver = webdriver.Chrome(options=options)
        case "edge":
            from selenium.webdriver.edge.options import Options
            options = Options()
            for argument in config.browser.OPTIONS_EDGE.split(';'):
                options.add_argument(argument)
            driver = webdriver.Edge(options=options)
        case _:
            raise RuntimeError(f"Browser {config.browser.NAME} is not supported.")
    driver.implicitly_wait(3)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture(scope="function")
def faker_data():
    fake = Faker()
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.ascii_free_email(),
        "password": fake.password(length=8)
    }


@pytest.fixture
def custom_base_url():
    return "https://magento.softwaretestingboard.com"

