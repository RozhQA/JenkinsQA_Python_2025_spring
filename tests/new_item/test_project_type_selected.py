from pages.new_item_page import NewItemPage
from tests.new_item.data import project_type_freestyle_title


def test_only_one_project_can_be_selected(new_item_page: NewItemPage):
    new_item_page.select_pipeline_project()
    new_item_page.select_freestyle_project()
    selected_items = new_item_page.get_selected_items()
    highlighted_items = new_item_page.get_highlighted_items()
    highlighted_title = new_item_page.get_title_highlighted_item()

    assert len(selected_items) == 1
    assert highlighted_items == selected_items
    assert highlighted_title == project_type_freestyle_title
