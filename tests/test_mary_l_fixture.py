from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def log_in(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_success_log_in(log_in):
    log_in.find_element(By.ID,"user-name").send_keys("standard_user")
    log_in.find_element(By.ID, "password").send_keys("secret_sauce")

    log_in.find_element(By.ID,"login-button").click()

    assert log_in.current_url == "https://www.saucedemo.com/inventory.html"


def test_locked_out_user(log_in):
    log_in.find_element(By.ID, "user-name").send_keys("locked_out_user")
    log_in.find_element(By.ID, "password").send_keys("secret_sauce")

    log_in.find_element(By.ID, "login-button").click()

    assert log_in.find_element(By.XPATH, '//*[@data-test="error"]').text == "Epic sadface: Sorry, this user has been locked out."