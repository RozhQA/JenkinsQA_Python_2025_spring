import requests
from requests.auth import HTTPBasicAuth

from tests.api.support.base_api import BaseAPI, logger


class JenkinsClient(BaseAPI):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        self.token, self.crumb_headers = self.generate_token("api-token")
        self.session.auth = HTTPBasicAuth(self.USERNAME, self.token)

    def post_xml(self, endpoint: str, xml_data: str):
        headers = {'Content-Type': 'application/xml'}
        headers.update(self.crumb_headers)
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.post(url, data=xml_data, headers=headers)

        if not response.ok:
            logger.error(response)
            return None
        return response
