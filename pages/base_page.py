from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.components.components import Header
from pages.ui_element import UIElementMixin


class BasePage(UIElementMixin):
    def __init__(self, driver: WebDriver, timeout = 5):
        super().__init__(driver)
        self.base_url = self.config.jenkins.base_url
        self.header = Header(driver)

    def open(self):
        self.driver.get(self.url)
        return self.wait_for_url()

    def wait_for_url(self):
        try:
            self.wait.until(EC.url_to_be(self.url))
            return self
        except TimeoutException:
            self.logger.error(f"Timeout when waiting for url {self.url}, current url: {self.driver.current_url}")
            raise

    def get_title(self) -> str:
        return self.driver.title
