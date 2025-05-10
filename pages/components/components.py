from selenium.webdriver.common.by import By

from pages.ui_element import UIElementMixin

class Header(UIElementMixin):
    class Locators:
        HEADER_LOGO = (By.ID, "jenkins-home-link")
        USER_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='/user/']")

    def go_to_the_main_page(self):
        from pages.main_page import MainPage
        return self.navigate_to(MainPage, self.Locators.HEADER_LOGO)

    def go_to_the_user_page(self):
        from pages.user_page import UserPage
        #self.wait_to_be_clickable(self.Locators.USER_PAGE_LINK).click()
        #return UserPage(self.driver, self.config.jenkins.USERNAME).wait_for_url()
        return self.navigate_to(UserPage, self.Locators.HEADER_LOGO, self.config.jenkins.USERNAME)
