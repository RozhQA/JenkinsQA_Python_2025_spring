import allure
import pytest

from tests.api.tests_ui.dashboard.data import DashboardTable, XmlConfigs


@pytest.fixture
@allure.step("Create Jenkins projects via API")
def create_projects_via_api(main_page, jenkins_steps):
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

    main_page.driver.refresh()
    return created
