import allure

from tests.pipeline.pipeline_data import BuildTriggers


@allure.epic("Pipeline Configuration")
@allure.story("Build Triggers")
@allure.title("Display the 'Enable or disable the current project' tooltip")
@allure.testcase("TC_04.001.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/542", name="Github issue")
def test_display_tooltip_enable_disable(multi_config_project_enabled):
    tooltip_enable_project = multi_config_project_enabled.get_switch_tooltip_text()

    assert tooltip_enable_project == ProjectToggle.TOOLTIP, \
        f"Expected tooltip {ProjectToggle.TOOLTIP} NOT FOUND"

    multi_config_project_enabled.click_switch_button().hover_over_help_discard_builds()
    tooltip_disable_project = multi_config_project_enabled.get_switch_tooltip_text()

    assert tooltip_disable_project == ProjectToggle.TOOLTIP, \
        f"Expected tooltip {ProjectToggle.TOOLTIP} NOT FOUND"