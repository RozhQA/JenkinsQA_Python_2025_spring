import allure


@allure.epic("Multibranch pipeline Configuration")
@allure.story("Change Properties")
@allure.title("Verify Properties section is available")
@allure.description("Verify that the “Properties” section is visible and accessible when editing a Multibranch Pipeline configuration in Jenkins.")
@allure.testcase("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/878", name="TC_06.010.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/878", name="Github issue")
def test_property_section_exists(multibranch_pipeline_config_page):
    properties_section = multibranch_pipeline_config_page.get_properties_section()

    with allure.step("Assert Properties section is displayed"):
        assert properties_section.is_displayed()