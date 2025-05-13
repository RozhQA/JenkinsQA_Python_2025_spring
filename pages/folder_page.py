from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FolderPage(BasePage):
    class Locators:
        EMPTY_STATE_MESSAGE = (By.XPATH, "//h2")
        CREATE_A_JOB = (By.CSS_SELECTOR, 'a[href="newJob"]')
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")
        SAVE_BUTTON = (By.XPATH, '//button[@name="Submit"]')
        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")

    def __init__(self, driver, folder_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(folder_name)}/"

    def get_empty_state_message(self):
        return self.wait_to_be_visible(self.Locators.EMPTY_STATE_MESSAGE).text

    def create_pipeline_in_folder(self, item_name):
        self.click_on(self.Locators.CREATE_A_JOB)
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(item_name)
        self.wait_to_be_clickable(self.Locators.ITEM_PIPELINE_PROJECT).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON)
        return self

    def get_item_list(self):
        return [item.text for item in self.find_elements(*self.Locators.TABLE_ITEM)]
