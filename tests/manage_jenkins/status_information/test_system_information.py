from pages.manage_jenkins.status_information.system_information_page import SystemInformationPage as SI


def test_open_system_information_page(manage_jenkins_page):
    sys_info_page = manage_jenkins_page.go_to_sys_info_page()
    assert sys_info_page.get_tabs_bar_headers() == SI.Data.TABS_BAR_HEADERS
