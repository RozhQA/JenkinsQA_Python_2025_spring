from pages.new_item_page import NewItemPage
from tests.new_item.data import new_folder_name


def test_health_metrics_available(new_item_page: NewItemPage):
    folder_conf_page = new_item_page.create_new_folder(new_folder_name)
    folder_conf_page.open()
    assert folder_conf_page.has_health_metrics_text_and_is_clickable(),\
        "'Health metrics' either not present or not clickable"



