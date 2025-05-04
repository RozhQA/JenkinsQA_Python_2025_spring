from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NewItemPage(BasePage):
    class Locator:
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        FOLDER_BUTTON = (By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')
        ITEM_LIST = (By.ID, "items")
        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
        ITEM_PIPELINE_PROJECT_ACTIVE = (By.CSS_SELECTOR, ".org_jenkinsci_plugins_workflow_job_WorkflowJob.active")
        ITEM_FREESTYLE_PROJECT = (By.CLASS_NAME, "hudson_model_FreeStyleProject")
        ITEM_FREESTYLE_PROJECT_ACTIVE = (By.CSS_SELECTOR, ".hudson_model_FreeStyleProject.active")
        SELECTED_ITEM = (By.XPATH, "//li[@aria-checked='true']")
        ACTIVE_ITEM = (By.CLASS_NAME, "active")
        ACTIVE_ITEM_TITLE = (By.XPATH, "//li[contains(@class, 'active')]//label/span")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/newJob"

    def create_new_folder(self, name):
        from pages.folder_config_page import FolderConfigPage
        self.wait_for_element(self.Locator.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locator.FOLDER_BUTTON).click()
        self.wait_to_be_clickable(self.Locator.OK_BUTTON).click()
        return FolderConfigPage(self.driver, name).wait_for_url()

    def select_pipeline_project(self):
        self.find_element(*self.Locator.ITEM_PIPELINE_PROJECT).click()
        self.wait_to_be_visible(self.Locator.ITEM_PIPELINE_PROJECT_ACTIVE)

    def select_freestyle_project(self):
        self.find_element(*self.Locator.ITEM_FREESTYLE_PROJECT).click()
        self.wait_to_be_visible(self.Locator.ITEM_FREESTYLE_PROJECT_ACTIVE)

    def get_selected_items(self):
        return self.find_elements(*self.Locator.SELECTED_ITEM)

    def get_highlighted_items(self):
        return self.find_elements(*self.Locator.ACTIVE_ITEM)

    def get_title_highlighted_item(self):
        return self.find_element(*self.Locator.ACTIVE_ITEM_TITLE).text.strip()
