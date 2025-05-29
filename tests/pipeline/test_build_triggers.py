import allure

from tests.pipeline.pipeline_data import BuildTriggers


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Displaying the \"Triggers\" section title")
@allure.testcase("TC_03.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/822", name="Github issue")
def test_display_triggers_section_header_description_menu(pipeline_config_page):
    title = pipeline_config_page.get_title_triggers()

    assert title == BuildTriggers.TITLE, f"Expected title '{BuildTriggers.TITLE}' NOT FOUND"
