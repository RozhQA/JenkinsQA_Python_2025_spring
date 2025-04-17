import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from core.settings import Config

load_dotenv()
base_url = os.getenv("APP_BASE_URL")

@pytest.fixture(scope="module")
def driver():
    config = Config.load()
    options = webdriver.ChromeOptions()
    options.add_argument(config.browser.OPTIONS_CHROME)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_success(driver):
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    driver.get(base_url)
    driver.find_element(By.ID, "user-name").send_keys(login)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    return driver

def test_add_to_cart(login_success, driver):
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart.text == "1", "not added to cart"