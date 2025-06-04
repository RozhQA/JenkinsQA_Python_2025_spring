import allure
from urllib.parse import quote
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PipelineConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        DESCRIPTION_FIELD = (By.NAME, 'description')
        SAVE_BUTTON = (By.NAME, "Submit")
        TITLE_TRIGGERS = (By.ID, "triggers")
        DESCRIPTION_TRIGGERS = (By.CSS_SELECTOR, "#triggers + .jenkins-section__description")
        SIDEBAR_TRIGGERS = (By.CSS_SELECTOR, "button[data-section-id='triggers']")
        TRIGGER_LABELS = (By.XPATH, "//span[input[contains(@name, 'Trigger')]]")
        TRIGGER_CHECKBOXES = (By.XPATH, "//*[contains(@name, 'Trigger') and @type='checkbox']")
        TRIGGER_CHECKBOX = (By.ID, "cb8")

    def __init__(self, driver, pipeline_name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.pipeline_name = pipeline_name
        self.url = self.base_url + f"/job/{quote(pipeline_name)}/configure"

    def wait_for_page(self):
        return self.wait_for_element(self.Locators.GENERAL_BUTTON)

    def add_description(self, text_for_description):
        self.wait_for_element(self.Locators.DESCRIPTION_FIELD).send_keys(text_for_description)
        return self

    def click_save_button(self, pipeline_project_name):
        from pages.pipeline_page import PipelinePage
        self.wait_to_be_clickable(self.Locators.SAVE_BUTTON).click()
        return PipelinePage(self.driver, pipeline_project_name).wait_for_url()

    @allure.step("Scroll to the \"Build Triggers\" section title")
    def scroll_to_triggers_section(self) -> None:
        element = self.wait_to_be_visible(self.Locators.TITLE_TRIGGERS)
        self.scroll_into_view(element)

    @allure.step("Get the title text for the \"Build Triggers\" section")
    def get_text_title_triggers(self) -> str:
        self.scroll_to_triggers_section()
        return self.get_visible_text(self.Locators.TITLE_TRIGGERS)

    @allure.step("Get the description text for the \"Build Triggers\" section")
    def get_text_description_triggers(self) -> str:
        self.scroll_to_triggers_section()
        return self.get_visible_text(self.Locators.DESCRIPTION_TRIGGERS)

    @allure.step("Get the sidebar label text for the \"Build Triggers\" section")
    def get_text_sidebar_triggers(self) -> str:
        return self.get_visible_text(self.Locators.SIDEBAR_TRIGGERS)

    @allure.step("Get text from all trigger checkbox labels")
    def get_text_trigger_labels(self) -> list[str]:
        self.scroll_to_triggers_section()
        labels = self.wait_to_be_visible_all(self.Locators.TRIGGER_LABELS)
        return [label.text.strip() for label in labels]

    @allure.step("Get visible of all trigger checkboxes ids")
    def get_visible_trigger_checkboxes_ids(self) -> list[str]:
        self.scroll_to_triggers_section()
        checkboxes = self.wait_to_be_visible_all(self.Locators.TRIGGER_CHECKBOXES)
        return [cb.get_attribute("id") for cb in checkboxes]

    @allure.step("Get trigger checkboxes checked states")
    def is_trigger_checkboxes_checked(self) -> list[bool]:
        return self.is_elements_selected(self.Locators.TRIGGER_CHECKBOXES)

    @allure.step("Get trigger checkboxes unchecked states")
    def is_trigger_checkboxes_unchecked(self) -> list[bool]:
        return self.is_elements_unselected(self.Locators.TRIGGER_CHECKBOXES)

    @allure.step("Clik all trigger checkbox labels")
    def click_trigger_labels(self):
        self.click_elements(self.Locators.TRIGGER_LABELS)
        return self
