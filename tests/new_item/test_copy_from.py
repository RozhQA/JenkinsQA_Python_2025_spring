from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .data_structs import NewItem, CopyFrom


def test_display_existing_item(prepare_new_item, config, wait):
    prepare_new_item.find_element(*CopyFrom.copy_from_selector).send_keys(
        CopyFrom.first_letter_of_name()
    )
    element = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "a.jenkins-dropdown__item"))
    )
    existing_item = element.text.strip()

    assert existing_item == NewItem.positive_name, (
        f"Expected item '{NewItem.positive_name}', but found '{existing_item}'"
    )
