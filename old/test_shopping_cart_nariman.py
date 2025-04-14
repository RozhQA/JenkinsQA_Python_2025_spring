from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import os
import time

def test_shopping_cart():
    chrome_options = Options()
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    item = driver.find_element(By.XPATH, "//div[.='Sauce Labs Backpack']")
    item.click()
    driver.find_element(By.ID, "add-to-cart").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    item_in_cart = driver.find_element(By.XPATH, "//div[.='Sauce Labs Backpack']")
    assert item_in_cart.text == 'Sauce Labs Backpack'
    driver.quit()