import pytest
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def fake_user_data() -> dict:
    def generate_wrong_email(email: str) -> str:
        error_type = random.choice(['insert space', 'remove at', 'remove dots'])
        if error_type == 'insert space':
            random_index = random.randint(1, len(email) - 2)
            return f'{email[:random_index]} {email[random_index:]}'
        elif error_type == 'remove_at':
            return email.replace('@', '')
        else:
            return email.replace('.', '')

    fake = Faker()
    fake_user_data = {
        "full_name": fake.name(),
        "valid_email": fake.email(),
        "current_address": fake.address().replace('\n', ' '),
        "permanent_address": fake.address().replace('\n', ' '),
        "wrong_email": generate_wrong_email(fake.email())
    }

    return fake_user_data


class BasePage:
    """Base class with common values and methods for all pages"""
    BASE_URL = 'https://demoqa.com'
    TIMEOUT = 5

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def send_keys(self, locator: tuple[str, str], text: str):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator: tuple[str, str]):
        self.driver.find_element(*locator).click()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_displayed(self, locator: tuple[str, str]) -> bool:
        return self.driver.find_element(*locator).is_displayed()


class ElementsTextBoxPage(BasePage):
    """Class with specific values and methods for Elements -> TextBox page"""
    URL = f'{BasePage.BASE_URL}/text-box'
    FULL_NAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    CURRENT_ADDRESS_FIELD = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_FIELD = (By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')
    SUBMITTED_FULL_NAME = (By.ID, 'name')
    SUBMITTED_EMAIL = (By.ID, 'email')
    SUBMITTED_CURRENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='currentAddress']")
    SUBMITTED_PERMANENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='permanentAddress']")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def submitted_element_text(self, locator: tuple[str, str]) -> str:
        return self.driver.find_element(*locator).text.split(':')[1]


class TestElementsTextBoxPage:
    def test_submit_all_correct_fields(self, driver: webdriver.Chrome, fake_user_data: dict):
        """Open https://demoqa.com/text-box and fill all fields with random correct data.
           Check that after click on "Submit" button correct data appears in output field."""
        page = ElementsTextBoxPage(driver)
        page.open()
        page.send_keys(page.FULL_NAME_FIELD, fake_user_data['full_name'])
        page.send_keys(page.EMAIL_FIELD, fake_user_data['valid_email'])
        page.send_keys(page.CURRENT_ADDRESS_FIELD, fake_user_data['current_address'])
        page.send_keys(page.PERMANENT_ADDRESS_FIELD, fake_user_data['permanent_address'])
        page.scroll_to_bottom()  # Otherwise submit button can be covered by advertising block
        page.click(page.SUBMIT_BUTTON)
        assert page.submitted_element_text(page.SUBMITTED_FULL_NAME) == fake_user_data['full_name']
        assert page.submitted_element_text(page.SUBMITTED_EMAIL) == fake_user_data['valid_email']
        assert page.submitted_element_text(page.SUBMITTED_CURRENT_ADDRESS) == fake_user_data['current_address']
        assert page.submitted_element_text(page.SUBMITTED_PERMANENT_ADDRESS) == fake_user_data['permanent_address']
