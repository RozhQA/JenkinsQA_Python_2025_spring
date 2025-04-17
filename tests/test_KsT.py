import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from core.settings import Config

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
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver

def test_add_to_cart(login_success, driver):
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart.text == "1", "not added to cart"