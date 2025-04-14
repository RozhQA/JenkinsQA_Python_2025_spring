import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def sauce(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_login(sauce):
    sauce.find_element(By.ID, "user-name").send_keys("standard_user")
    sauce.find_element(By.ID, "password").send_keys("secret_sauce")
    sauce.find_element(By.ID, "login-button").click()
    sauce.back()
    title = sauce.find_element(By.XPATH, "//*[@class = 'login_logo']").text
    assert title == "Swag Labs"



def test_error_not_displayed_after_refresh_page_login_page(sauce):
    sauce.find_element(By.ID, "login-button").click()

    error_el = sauce.find_element(By.XPATH, "//*[contains(text(),'Username is required')]")
    assert error_el.is_displayed(), "Error should be visible before refresh"
    sauce.refresh()

    try:
        error_el_after_refresh = sauce.find_element(By.XPATH, "//*[contains(text(),'Username is required')]")
        error_is_visible_after_refresh = error_el_after_refresh.is_displayed()
    except NoSuchElementException:
        error_is_visible_after_refresh = False

    assert not error_is_visible_after_refresh, "Error message is still showing after page refresh"
