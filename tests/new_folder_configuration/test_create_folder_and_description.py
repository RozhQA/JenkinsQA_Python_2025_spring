from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_create_folder_without_description(main_page, create_folder):
    # TC_05.001.02
    wait = WebDriverWait(main_page, 10)
    item_display_name = "Sanity tests"
    # Folder creation is placed in the custom conftest.py file
    create_folder(item_display_name)
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    # Press submit button without filling the fields
    main_page.find_element(By.CSS_SELECTOR, "[name='Submit']").click()
    # Check results
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h4")))
    # Find folder name
    check_display_name_element = main_page.find_element(By.XPATH, "//*[@id='main-panel']/h1")
    check_display_name = check_display_name_element.text
    print("Folder name: ", check_display_name)
    # Find description - it should be empty
    check_description_element = main_page.find_element(By.XPATH, "//*[@id='view-message']")
    check_description = check_description_element.text
    print("Description: ", check_description)

    assert check_display_name == item_display_name, "Folder name is incorrect"
    assert check_description == "", "Description is present"

# Аутпут, если создать папку без описания и отображаемого имени:
# Captured folder name:  None
# Displayed name:  Sanity tests
# Description:


def test_create_folder_with_description_only(main_page, create_folder):
    # TC_05.001.01
    wait = WebDriverWait(main_page, 10)
    item_name = "Folder one"
    item_description = "This is a sanity test"
    # Folder creation is placed in the custom conftest.py file
    create_folder(item_name)
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    # Fill in Description field
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> textarea").send_keys(item_description)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='Submit']"))).click()
    # Check results
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h4")))
    # receive two fields
    check_display_name_element = main_page.find_element(By.XPATH, "//*[@id='main-panel']/h1")
    check_display_name = check_display_name_element.text
    print("Folder name: " + check_display_name)
    check_description_element = main_page.find_element(By.XPATH, "//*[@id='view-message']")
    check_description = check_description_element.text
    print("Description: " + check_description)

    assert check_display_name == item_name, "Folder name is incorrect"
    assert check_description == item_description, "Description is incorrect"

def test_create_folder_with_display_and_description(main_page, create_folder):
    # TC_05.001.03
    wait = WebDriverWait(main_page, 10)
    item_name = "Folder one"
    item_display_name = "My first folder"
    item_description = "This is a sanity test"
    # Folder creation is placed in the custom conftest.py file
    create_folder(item_name)
    wait.until(EC.visibility_of_element_located((By.ID, "general")))
    # Fill in Display Name field
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> input").send_keys(item_display_name)
    # Fill in Description field
    main_page.find_element(By.CSS_SELECTOR, "div.setting-main> textarea").send_keys(item_description)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='Submit']"))).click()
    # Check results
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h4")))
    main_panel = main_page.find_element(By.ID, "main-panel")
    text = main_panel.text
    # receive "Folder name:"
    check_name = None
    for line in text.splitlines():
        if line.strip().startswith("Folder name:"):
            check_name = line.strip()
    print("Captured folder name: " + check_name)
    # receive "Display name" and "Description"
    check_display_name_element = main_page.find_element(By.XPATH, "//*[@id='main-panel']/h1")
    check_display_name = check_display_name_element.text
    print("Displayed name: " + check_display_name)
    check_description_element = main_page.find_element(By.XPATH, "//*[@id='view-message']")
    check_description = check_description_element.text
    print("Description: " + check_description)

    assert check_name == "Folder name: " + item_name, "Folder name is incorrect"
    assert check_display_name == item_display_name, "Display name is incorrect"
    assert check_description == item_description, "Description is incorrect"

