import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def heroku_driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_successful_login(heroku_driver):
    heroku_driver.find_element(By.ID, "username").send_keys("tomsmith")
    heroku_driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    heroku_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(10)

    success_message = heroku_driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message