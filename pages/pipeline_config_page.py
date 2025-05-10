from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PipelineConfigPage(BasePage):

    class Locator:
        DESCRIPTION_FIELD = (By.NAME, 'description')
        SAVE_BUTTON = (By.NAME, "Submit")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.name = name
        self.url = self.base_url + f"/job/{name}/configure"

    def add_description(self, text_for_description):
        self.wait_for_element(self.Locator.DESCRIPTION_FIELD).send_keys(text_for_description)
        return self

    def click_save_button(self):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locator.SAVE_BUTTON).click()
        return PipelinePage(self.driver, pipeline_project_name=self.name).wait_for_url()
