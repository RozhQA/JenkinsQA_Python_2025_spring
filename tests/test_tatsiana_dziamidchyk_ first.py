from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_successful_login():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)

    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message

    driver.quit()