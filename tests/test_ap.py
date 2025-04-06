import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC

LOGIN_PAGE_URL = "https://www.saucedemo.com/"
PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

STANDARD_USER_name = "standard_user"
USER_PASSWORD = "secret_sauce"
USER_NAME_FIELD = (By.XPATH, "//input[@id='user-name']")
USER_PWD_FIELD = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LOGOUT_BUTTON = (By.CSS_SELECTOR, "#logout_sidebar_link")


def login_as_standard_user(driver):
    WAIT(driver, 23).until(EC.visibility_of_element_located(USER_NAME_FIELD)).send_keys(STANDARD_USER_name)
    WAIT(driver, 23).until(EC.visibility_of_element_located(USER_PWD_FIELD)).send_keys(USER_PASSWORD)
    WAIT(driver, 23).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()


class TestSauceDemo:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
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



