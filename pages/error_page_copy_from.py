from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ErrorPageCopyFrom(BasePage):
    class Locators:
        ERROR_HEADER = (By.CSS_SELECTOR, "#main-panel > h1")
        ERROR_TEXT = (By.CSS_SELECTOR, "#main-panel > p")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        self.url = self.base_url + "/view/all/createItem"

    def get_header_error(self):
        return self.wait_for_element(self.Locators.ERROR_HEADER).text.strip()

    def get_message_error(self):
        return self.wait_for_element(self.Locators.ERROR_TEXT).text.strip()
