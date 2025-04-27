import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def wait5(main_page):
    wait5 = WebDriverWait(main_page, 5)
    return wait5

def test_empty_name(new_item_page, wait5):
    wait5.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "jenkins-form-label"))
    ).click()
    error_message = wait5.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "input-validation-message"))
    )

    assert error_message.value_of_css_property("color") in ("rgb(230, 0, 31)", "rgba(230, 0, 31, 1)")
