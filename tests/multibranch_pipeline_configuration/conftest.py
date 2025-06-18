import pytest
import allure

from pages.new_item_page import NewItemPage
from pages.multibranch_pipeline_config_page import MultibranchPipelineConfigPage
from tests.multibranch_pipeline_configuration.mbp_data import Project


@pytest.fixture(scope='function')
@allure.title(f"Create new multibranch pipeline project with name \"{Project.PROJECT_NAME}\"")
def multibranch_pipeline_config_page(new_item_page:NewItemPage) -> MultibranchPipelineConfigPage:
    return new_item_page.create_new_multibranch_pipeline_project(Project.PROJECT_NAME)