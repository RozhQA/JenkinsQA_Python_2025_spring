from pages.manage_jenkins.status_information.system_information_page import SystemInformationPage as SI


def test_open_system_information_page(manage_jenkins_page):
    system_information_page = manage_jenkins_page.go_to_the_system_information_page()
    assert system_information_page.is_visible(SI.Locator.TABS_BAR), "Tabs bar is not displayed"


