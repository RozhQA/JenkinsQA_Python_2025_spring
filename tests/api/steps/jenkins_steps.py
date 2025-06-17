import allure

from tests.api.support.jenkins_client import JenkinsClient


class JenkinsSteps:
    def __init__(self, client: JenkinsClient):
        self.client = client

    @allure.step('POST /createItem')
    def post_create_item(self, project_name: str, config_xml: str) -> bool:
        response = self.client.post_xml(f"createItem?name={project_name}", config_xml)

        if response and response.ok:
            allure.attach(config_xml, name=f"[Created]{project_name}", attachment_type=allure.attachment_type.XML)
            return True
        else:
            msg = response.text if response else "No response"
            allure.attach(msg, name=f"[Failed]{project_name}", attachment_type=allure.attachment_type.TEXT)
            return False
