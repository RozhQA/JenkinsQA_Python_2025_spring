import pytest

from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


@pytest.fixture
def create_job_and_folders(new_item_page):
    """
    Fixture that creates a test environment with:
    1. A multi-configuration project
    2. A folder containing a pipeline job
    return main page for test assertions
    """

    return new_item_page.create_new_multi_config_project(new_multi_config_project_name) \
                        .header.go_to_the_main_page() \
                        .go_to_new_item_page() \
                        .create_new_folder(new_folder_name) \
                        .header.go_to_the_main_page() \
                        .click_on_folder_item(new_folder_name) \
                        .create_new_job() \
                        .create_pipeline(new_pipeline_name) \
                        .header.go_to_the_main_page()
