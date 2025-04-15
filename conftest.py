import os
import sys
import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.jenkins_utils import clear_data
from core.settings import Config


project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config():
    return Config.load()


@pytest.fixture(scope="function", autouse=True)
def jenkins_reset(config):
    clear_data(config)


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
def login_page(driver: WebDriver, config):
    driver.get(config.jenkins.base_url + "/login?from=%2F")
    return driver


@pytest.fixture(scope="function")
def main_page(login_page: WebDriver, config):
    login_page.find_element(By.NAME, "j_username").send_keys(config.jenkins.USERNAME)
    login_page.find_element(By.NAME, "j_password").send_keys(config.jenkins.PASSWORD)
    login_page.find_element(By.NAME, "Submit").click()
    WebDriverWait(login_page, 5).until(EC.url_changes(config.jenkins.base_url + "/login?from=%2F"))
    return login_page

