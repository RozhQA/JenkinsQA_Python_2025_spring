from time import sleep  # noqa: D100
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome Ignore SSL Err Settings
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

Expected_City = "Барнаул"


# On-Site Actions
def Login_Sequence_With_City_Change():
    """Helix.ru change city test."""
    driver.get("https://helix.ru")
    sleep(2)  # Prevent 404 page site bug, NOT DEBUG
    # Press NO to SPB
    driver.find_element(By.XPATH, '//button[@data-testid="reject-city-button"]').click()  # noqa: E501,PLC301

    # Found City via search field
    input_city_field = driver.find_element(By.XPATH, '//app-city//input[@type="search"]')  # noqa: E501,PLC301
    input_city_field.send_keys(Expected_City)
    sleep(3)  # Page Update Time, required, NOT DEBUG
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal-container/div/div/div/app-city/div[2]/div[2]/app-city-search/div/div/span").click()  # noqa: E501,PLC301

    # Check Current Selected City on Main Page
    sleep(3)  # Page Update Time, required, NOT DEBUG
    Current_City = driver.find_element(By.XPATH, "/html/body/app-helix/app-helix-header/div[1]/div[2]/div/div/div[1]/div/div[1]/div/span/span[1]").text  # noqa: E501,PLC301
    assert Current_City == Expected_City, ("Expected City Not Recieved")  # noqa: S101, PLC301, E501

    # Go to login page
    driver.find_element(By.XPATH, "/html/body/app-helix/app-helix-header/div[1]/div[3]/div/div/div[5]/a").click()  # noqa: E501
    # Fill input fields
    driver.find_element(By.ID, "email").send_keys("testmi-1@ya.ru")
    driver.find_element(By.ID, "pass").send_keys("asdASD11!!")
    # Press button
    driver.find_element(By.ID, "loginLKK").click()
    sleep(3)  # Page load delay, NOT DEBUG
    driver.get("https://helix.ru")
    sleep(3)  # Page load delay, NOT DEBUG
    Uname = driver.find_element(By.XPATH, "/html/body/app-helix/app-helix-header/div[1]/div[3]/div/div/div[6]/app-user-info-button/div/div[1]/div/div").text  # noqa: E501
    assert Uname == "For Showing Cutout behavior at long S.", ("Expected Username Not Recieved")  # noqa: E501


driver = webdriver.Chrome(options)  # Chrome usage
Login_Sequence_With_City_Change()
driver.close()

driver = webdriver.Firefox()  # FF usage
Login_Sequence_With_City_Change()
driver.close()
