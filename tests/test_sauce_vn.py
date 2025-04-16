import time
from logging import exception

import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException


LOGIN_PAGE = "https://www.saucedemo.com/"
PRODUCT_PAGE = "https://www.saucedemo.com/inventory.html"


@pytest.fixture
def sauce(driver):
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    driver.get(LOGIN_PAGE)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login(sauce):
    sauce.find_element(By.ID, 'user-name').send_keys("standard_user")
    sauce.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce.find_element(By.NAME, 'login-button').click()


def test_login(sauce, login):
    assert sauce.current_url == PRODUCT_PAGE


def test_open_sidebar_menu(sauce, login):
    sauce.find_element(By.XPATH, "//button[text()='Open Menu']").click()
    assert sauce.find_element(By.XPATH, "// a[text() = 'About']")


def test_add_item_to_cart(sauce, login):
    sauce.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    sauce.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

    assert sauce.current_url == "https://www.saucedemo.com/cart.html"

def test_check_item_in_cart(sauce, login):
    sauce.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    sauce.find_element(By.XPATH, "//a[@class = 'shopping_cart_link']").click()

    assert sauce.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='cart_item']")

def test_open_item(sauce, login):
    sauce.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Fleece Jacket')]").click()

    assert sauce.current_url == "https://www.saucedemo.com/inventory-item.html?id=5"


def test_locked_out_user(sauce):

    sauce.find_element(By.ID, 'user-name').send_keys("locked_out_user")
    sauce.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce.find_element(By.NAME, 'login-button').click()

    error_message = sauce.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."


def test_invalid_password(sauce):

    sauce.find_element(By.ID, 'user-name').send_keys("standard_user")
    sauce.find_element(By.ID, 'password').send_keys("secret")
    sauce.find_element(By.NAME, 'login-button').click()

    error_message = sauce.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"


def test_empty_username_field(sauce):

    sauce.find_element(By.ID, 'password').send_keys("secret_sauce")
    sauce.find_element(By.NAME, 'login-button').click()

    error_message = sauce.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"



def test_empty_password_field(sauce):

    sauce.find_element(By.ID, 'user-name').send_keys("standard_user")
    sauce.find_element(By.NAME, 'login-button').click()

    error_message = sauce.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Password is required"


def test_empty_username_password_fields(sauce):

    sauce.find_element(By.NAME, 'login-button').click()

    error_message = sauce.find_element(By.XPATH, '//h3[@data-test= "error"]')
    assert error_message.text == "Epic sadface: Username is required"


def test_logout(sauce, login):
    sauce.find_element(By.XPATH, "//button[text()='Open Menu']").click()

    WebDriverWait(sauce, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()
    WebDriverWait(sauce, 5).until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

    assert sauce.current_url == LOGIN_PAGE