import allure
import pytest_check as check

from tests.pipeline.pipeline_data import BuildTriggers


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section title")
@allure.testcase("TC_03.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/822", name="Github issue")
def test_display_triggers_section_title(pipeline_project_config_page):
    assert pipeline_project_config_page.get_title_triggers() == BuildTriggers.TITLE, \
        f"Expected title '{BuildTriggers.TITLE}' NOT FOUND"


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section description")
@allure.testcase("TC_03.003.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/831", name="Github issue")
def test_display_triggers_section_description(pipeline_project_config_page):
    assert pipeline_project_config_page.get_description_triggers() == BuildTriggers.DESCRIPTION, \
        f"Expected description '{BuildTriggers.DESCRIPTION}' NOT FOUND"


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section in the sidebar")
@allure.testcase("TC_03.003.03")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/832", name="Github issue")
def test_display_triggers_section_in_sidebar(pipeline_project_config_page):
    assert pipeline_project_config_page.get_sidebar_triggers() == BuildTriggers.TITLE, \
        f"Expected title in the sidebar '{BuildTriggers.TITLE}' NOT FOUND"


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying trigger checkbox labels")
@allure.testcase("TC_03.003.04")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/833", name="Github issue")
def test_display_trigger_checkbox_labels(pipeline_project_config_page):
    actual_labels = pipeline_project_config_page.get_text_trigger_labels()
    for expected_label in BuildTriggers.TRIGGER_LABELS:
        check.is_in(expected_label, actual_labels, f"Expected label '{expected_label}' NOT FOUND {actual_labels}")
