import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def sauce(driver):
    driver.get("https://www.saucedemo.com/")
    return driver


def test_locked_out_user_error_message(sauce):
    sauce.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    sauce.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce.find_element(By.NAME, 'login-button').click()

    error_message = sauce.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."


def test_locked_out_user_url_check(sauce):
    sauce.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    sauce.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce.find_element(By.NAME, 'login-button').click()

    assert sauce.current_url == "https://www.saucedemo.com/", "wrong url"


def test_jenkins(login_page):
    assert login_page.title == 'Sign in [Jenkins]', "wrong title"


def test_jenkins_main_page(main_page):
    assert main_page.title == 'Dashboard [Jenkins]', "wrong title"
