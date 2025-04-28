from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_access_appearance_section(main_page, open_appearance_page):
    header = WebDriverWait(main_page, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Appearance')]"))
    )
    assert "Appearance" in header.text
