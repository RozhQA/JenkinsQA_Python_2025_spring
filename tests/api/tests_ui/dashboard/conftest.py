import allure
import pytest

from tests.api.tests_ui.dashboard.data import DashboardTable, XmlConfigs
from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


@allure.title("API: Prepare env > Create jobs and folders")
@pytest.fixture
def create_job_and_folders_api(jenkins_steps):
    jenkins_steps.post_create_item(new_multi_config_project_name, XmlConfigs.MULTI_CONFIGURATION_PROJECT)
    jenkins_steps.post_create_item(new_folder_name, XmlConfigs.FOLDER)
    jenkins_steps.post_create_item_in_folder(new_folder_name, new_pipeline_name, XmlConfigs.PIPELINE)


@allure.title("API: Prepare env > Create all types of projects")
@pytest.fixture
def create_projects_via_api(jenkins_steps):
    project_configs = {
        "Freestyle project": XmlConfigs.FREESTYLE_PROJECT,
        "Pipeline": XmlConfigs.PIPELINE,
        "Multi-configuration project": XmlConfigs.MULTI_CONFIGURATION_PROJECT,
        "Folder": XmlConfigs.FOLDER,
        "Multibranch Pipeline": XmlConfigs.MULTIBRANCH_PIPELINE,
        "Organization Folder": XmlConfigs.ORGANIZATION_FOLDER,
    }
    created = []

    for project_type, project_name in DashboardTable.PROJECT_NAMES.items():
        config_xml = project_configs.get(project_type)
        jenkins_steps.post_create_item(project_name, config_xml)
        created.append((project_type, project_name))

    return created
