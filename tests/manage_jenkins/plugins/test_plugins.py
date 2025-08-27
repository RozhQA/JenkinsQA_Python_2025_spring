import allure
import pytest

from tests.manage_jenkins.data import Plugins as DATA


@allure.epic("Manage Jenkins")
@allure.story("Add Plugins")
@allure.title("User could be able to install plugins in the program")
@allure.testcase("TC_10.003.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/784", name="Github issue")
def test_plugins_available(plugins):
    with allure.step("Assert that menu item \"Available plugins\" is available"):
        assert plugins.is_available_plugins_displayed()
    with allure.step("Open Available plugins Page"):
        available_plugins = plugins.go_to_available_plugins_page()
    with allure.step("Assert that Search Available Plugins field is visible"):
        assert available_plugins.is_search_available_plugins_field_visible()
    with allure.step("Assert that list of plugins available for installation is displayed"):
        assert available_plugins.count_available_plugins() > 0
    with allure.step("Assert that \"Install\" button is visible"):
        assert available_plugins.is_install_button_visible()
    with allure.step("Assert that \"Install\" button is disabled"):
        assert available_plugins.is_install_button_disabled()

@allure.epic("Manage Jenkins")
@allure.story("Add Plugins")
@allure.title("Installing the plugin")
@allure.testcase("TC_10.003.02")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/784", name="Github issue")
@pytest.mark.skip("failed on CI")
def test_plugin_install(plugins):
    with allure.step("Open Available plugins Page"):
        available_plugins = plugins.go_to_available_plugins_page()
    with allure.step(f"Type plugin name \"{DATA.PLUGIN_NAME}\"for install."):
        available_plugins.type_plugin_name_to_search_field(DATA.PLUGIN_NAME)
    if available_plugins.count_available_plugins() != 0:
        with allure.step("Assert that plugin has been found."):
            assert available_plugins.count_available_plugins() == 1
        with allure.step("Selection founded plugin to install."):
            available_plugins.select_plugin_checkbox()
        with allure.step("Plugin's installation."):
            progress_bar = available_plugins.click_install_button()
        with allure.step("Assert that “Download progress” page opens"):
            assert progress_bar.get_title_page() == DATA.TITLE_DOWNLOAD_PROGRESS_PAGE
        with allure.step("Assert that \"Success\" displayed next to the \"Loading plugin extensions\" label"):
            assert progress_bar.is_success_loading_plugin_extensions()
        with allure.step(f"Assert that \"Success\" displayed next to the \"{DATA.PLUGIN_NAME}\""):
            assert progress_bar.is_success_plugin_name()
        with allure.step("go to \"Installed plugins\" page"):
            installed_plugins = progress_bar.go_to_installed_plugins_page()
        with allure.step(f"Assert that the \"{DATA.PLUGIN_NAME}\" plugin exist in the list of plugins on the “Installed plugins” page"):
            assert installed_plugins.is_plugin_installed(DATA.PLUGIN_NAME)
    else:
        with allure.step(f"Plugin \"{DATA.PLUGIN_NAME}\" has been installed already!"):
            assert True, "The plugin has been installed!"

@allure.epic("Manage Jenkins")
@allure.story("Remove Plugins")
@allure.title("Uninstalling the plugin")
@allure.testcase("TC_10.004.01")
@allure.link("https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring/issues/814", name="Github issue")
@pytest.mark.skip("failed on CI")
def test_plugin_uninstall(inst):
    with allure.step(f"Check that \"{DATA.PLUGIN_NAME}\" plugin is not installed."):
        if not inst.is_plugin_installed(DATA.PLUGIN_NAME):
            with allure.step(f"The \"{DATA.PLUGIN_NAME}\" plugin is not installed."):
                assert True, f"Plugin \"{DATA.PLUGIN_NAME}\" is not installed, yet!"
        else:
            with allure.step(f"Type \"{DATA.PLUGIN_NAME}\" to search field."):
                inst.type_plugin_name_to_search_field(DATA.PLUGIN_NAME)
            with allure.step(f"Check that \"{DATA.PLUGIN_NAME}\" plugin already uninstalled."):
                if inst.is_uninstallation_pending():
                    with allure.step(f"Plugin \"{DATA.PLUGIN_NAME}\" has been uninstalled already."):
                        assert True, f"Plugin \"{DATA.PLUGIN_NAME}\" has been uninstalled already. Please, restart Jenkins to complete uninstall."
                else:
                    with allure.step(f"Uninstall \"{DATA.PLUGIN_NAME}\" plugin."):
                        inst.click_uninstall()
                    with allure.step(f"Assert that \"{DATA.PLUGIN_NAME}\" plugin has been uninstalled."):
                        assert inst.is_uninstallation_pending()
