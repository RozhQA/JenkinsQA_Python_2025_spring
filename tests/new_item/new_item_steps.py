from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from .data_structs import NewItem, FreestyleItem


def create_item(new_item_page: WebDriver, config):
    new_item_page.find_element(*NewItem.name_field_selector).send_keys(NewItem.positive_name)
    new_item_page.find_element(*FreestyleItem.freestyle_selector).click()
    wait = WebDriverWait(new_item_page, 15)
    wait.until(EC.element_to_be_clickable(FreestyleItem.ok_button_selector)).click()
    config_url = config.jenkins.base_url + FreestyleItem.configuration_page
    wait.until(EC.url_to_be(config_url))
    new_item_page.find_element(*FreestyleItem.save_button_selector).click()
    item_url = config.jenkins.base_url + FreestyleItem.item_page
    wait.until(EC.url_to_be(item_url))
    new_item_page.get(config.jenkins.base_url + NewItem.url)
    wait.until(EC.url_to_be(config.jenkins.base_url + NewItem.url))

    return new_item_page
