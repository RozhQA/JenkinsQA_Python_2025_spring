from selenium.webdriver.common.by import By
from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage


class SystemInformationPage(ManageJenkinsPage):
    class Locator:
        TABS_BAR = (By.CSS_SELECTOR, ".tabBar")

    class Data:
        TABS_BAR_HEADERS = [
            "System Properties",
            "Environment Variables",
            "Plugins",
            "Memory Usage",
            "Threads"
        ]

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/manage/systemInfo"
