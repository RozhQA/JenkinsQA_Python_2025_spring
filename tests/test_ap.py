import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC

LOGIN_PAGE_URL = "https://www.saucedemo.com/"
PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

# locators
USER_NAME_FIELD = (By.XPATH, "//input[@id='user-name']")
USER_PWD_FIELD = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_sidebar_link")

# test_data
STANDARD_USER_name = "standard_user"
USER_PASSWORD = "secret_sauce"
USERNAME_REQUIRED_ERROR_MSG = "Epic sadface: Username is required"
PASSWORD_REQUIRED_ERROR_MSG = "Epic sadface: Password is required"
PASSWORD_FIELD_TYPE = 'password'


def login_as_standard_user(driver):
    WAIT(driver, 23).until(EC.visibility_of_element_located(USER_NAME_FIELD)).send_keys(STANDARD_USER_name)
    WAIT(driver, 23).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)
    WAIT(driver, 23).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()


def assert_error_message(driver, error_message):
    actual_error_message = (WAIT(driver, 23)
                            .until(EC.visibility_of_element_located((By.XPATH, "//h3"))).text)
    assert actual_error_message == error_message


class TestSauceDemo:

    @pytest.fixture
    def driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-cache")
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_login_standard_user(self, driver):
        driver.get(LOGIN_PAGE_URL)

        login_as_standard_user(driver)
        assert driver.current_url == PRODUCTS_PAGE_URL

    def test_standard_user_logout(self, driver):
        driver.get(LOGIN_PAGE_URL)

        login_as_standard_user(driver)
        WAIT(driver, 23).until(EC.visibility_of_element_located(BURGER_MENU)).click()
        WAIT(driver, 23).until(EC.visibility_of_element_located(LOGOUT_BUTTON)).click()

        assert driver.current_url == LOGIN_PAGE_URL

    def test_username_required(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WAIT(driver, 23).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)
        WAIT(driver, 23).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()

        assert_error_message(driver, USERNAME_REQUIRED_ERROR_MSG)

    def test_password_required(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WAIT(driver, 23).until(EC.visibility_of_element_located(USER_NAME_FIELD)).send_keys(STANDARD_USER_name)
        WAIT(driver, 23).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()

        assert_error_message(driver, PASSWORD_REQUIRED_ERROR_MSG)

    def test_password_masked_by_bullets(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WAIT(driver, 23).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)

        password_field_type = (WAIT(driver, 23).until(EC.visibility_of_element_located(USER_PWD_FIELD))
                               .get_attribute('type'))

        assert password_field_type == PASSWORD_FIELD_TYPE
