import os
import sys
import logging

import pytest

from selenium import webdriver


from core.jenkins_utils import clear_data
from core.settings import Config


project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config():
    return Config.load()


@pytest.fixture(scope="function")
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

