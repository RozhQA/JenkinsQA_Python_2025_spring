from time import sleep  # noqa: D100
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome Ignore SSL Err Settings
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')


# On-Site Actions
def Change_City():
    """Helix.ru change city test."""
    driver.get("https://helix.ru")
    sleep(2)  # Prevent 404 page site bug, NOT DEBUG
    # Press NO to SPB
    driver.find_element(By.CSS_SELECTOR, "div.row-item:nth-child(2) > button:nth-child(1)").click()  # noqa: E501,PLC301

    # Found City via search field
    input_city_field = driver.find_element(By.CSS_SELECTOR, '#cdk-overlay-1 > nz-modal-container > div > div > div > app-city > div.grid.grid-gutter-16.grid-column.overflow-hidden > div:nth-child(1) > input')  # noqa: E501,PLC301
    input_city_field.send_keys(Expected_City)
    sleep(3)  # Page Update Time, required, NOT DEBUG
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal-container/div/div/div/app-city/div[2]/div[2]/app-city-search/div/div/span").click()  # noqa: E501,PLC301

    # Check Current Selected City on Main Page
    sleep(3)  # Page Update Time, required, NOT DEBUG
    Current_City = driver.find_element(By.XPATH, "/html/body/app-helix/app-helix-header/div[1]/div[2]/div/div/div[1]/div/div[1]/div/span/span[1]").text  # noqa: E501,PLC301
    assert Current_City == Expected_City, ("Expected City Not Recieved")  # noqa: S101, PLC301, E501


Expected_City = "Барнаул"

driver = webdriver.Chrome(options)  # Chrome usage
Change_City()
driver.close()

driver = webdriver.Firefox()  # FF usage
Change_City()
driver.close()
