import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def open_appearance_page(main_page, config):
        manage_url = f"{config.jenkins.base_url}/manage"
        main_page.get(manage_url)
        appearance_link = WebDriverWait(main_page, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="appearance"]'))
        )
        appearance_link.click()
        WebDriverWait(main_page, 10).until(EC.url_contains("appearance"))
