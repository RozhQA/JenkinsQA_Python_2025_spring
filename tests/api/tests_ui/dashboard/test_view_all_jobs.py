import allure

from tests.api.tests_ui.dashboard.data import DashboardTable


@allure.epic("Dashboard with the items")
@allure.story("View All Jobs")
@allure.title("API:Verification of default state for job without configuration")
@allure.description("Verify that a newly created job without any build history or configuration displays the correct"
                    " default state in the dashboard jobs table.")
@allure.testcase("TC_12.001.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/757", name="Github issue")
def test_verify_default_state_for_all_project(main_page, create_projects_via_api):
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
