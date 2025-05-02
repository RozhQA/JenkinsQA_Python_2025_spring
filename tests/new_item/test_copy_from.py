from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .data_structs import NewItem, CopyFrom


def test_display_existing_item(prepare_new_item, config, wait):
    prepare_new_item.find_element(*CopyFrom.copy_from_field_selector).send_keys(
        CopyFrom.get_first_letter_of_project_name()
    )
    existing_item = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "a.jenkins-dropdown__item"
    )))
    actual_item_text = existing_item.text.strip()

    assert actual_item_text == NewItem.positive_name, (
        f"Expected item '{NewItem.positive_name}', but found '{actual_item_text}'"
    )
