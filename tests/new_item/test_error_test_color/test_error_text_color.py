import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def wait5(main_page):
    wait5 = WebDriverWait(main_page, 5)
    return wait5

@pytest.fixture
def new_items(main_page,wait5):

    main_page.find_element(By.XPATH, "//a[contains(., 'New Item')]").click()
    wait5 .until(
        EC.element_to_be_clickable((By.CLASS_NAME, "jenkins-form-label"))
    ).click()


@pytest.mark.usefixtures("new_items")
def test_empty_name(main_page, wait5):
    error_message = wait5.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "input-validation-message"))
    )

    assert (
            error_message.text == "» This field cannot be empty, please enter a valid name"
            and error_message.value_of_css_property("color") in ("rgb(230, 0, 31)", "rgba(230, 0, 31, 1)")
    )