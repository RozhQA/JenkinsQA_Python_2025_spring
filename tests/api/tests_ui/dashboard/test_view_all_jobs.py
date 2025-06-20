import allure

from tests.api.tests_ui.dashboard.data import DashboardTable
from tests.new_item.data import new_folder_name, new_pipeline_name, new_multi_config_project_name


@allure.epic("Dashboard with the items")
@allure.story("View All Jobs")
@allure.title("API: Display list of jobs and folders")
@allure.description("Verify that all jobs and folders are listed on the Dashboard page.")
@allure.testcase("TC_12.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/688", name="Github issue")
def test_all_jobs_and_folders_visible_in_dashboard(create_job_and_folders_api, main_page):
    items = main_page.get_item_list()
    assert new_multi_config_project_name in items, "Multi-conf project should be visible on Dashboard"
    assert new_folder_name in items, "Folder should be visible on Dashboard"
    assert new_pipeline_name not in items, "Pipeline job should only be visible inside its folder"

    folder_contents = main_page.go_to_the_folder_page(new_folder_name).get_item_list()
    assert new_pipeline_name in folder_contents, "Pipeline job should be visible when opening its folder"


@allure.epic("Dashboard with the items")
@allure.story("View All Jobs")
@allure.title("API: Verification of default state for job without configuration")
@allure.description("Verify that a newly created job without any build history or configuration displays the correct"
                    " default state in the dashboard jobs table.")
@allure.testcase("TC_12.001.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/757", name="Github issue")
def test_verify_default_state_for_all_project(create_projects_via_api, main_page):
    # main_page.driver.refresh()
    allure.attach(
        main_page.driver.get_screenshot_as_png(),
        name="Dashboard view with all created projects",
        attachment_type=allure.attachment_type.PNG
    )
    for project_type, project_name in create_projects_via_api:
        with allure.step(f"Check default state for item '{project_name}'"):
            with allure.step(f"Load expected data for item '{project_type}'"):
                expected_data = DashboardTable.DEFAULT_PROJECT_DATA_MAP[project_type].copy()
                expected_data["name"] = project_name
            actual_info = main_page.get_project_row_data(project_name)
            assert actual_info == list(expected_data.values()), \
                f"Mismatch for project '{project_type}'. Expected: {list(expected_data.values())}, Actual: {actual_info}"
