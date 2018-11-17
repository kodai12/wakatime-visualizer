import requests
import base64
import os

from app.domain.model.user import User
from app.anticorruption.wakatime.api import WakatimeUserTranslator

class WakatimeAPIDataSource:
    def __init__(self):
        if 'WAKATIME_API_KEY' not in os.environ:
            print('os.environ[\'WAKATIME_API_KEY\'] is NOT set!!')
            raise
        self.api_key = os.environ['WAKATIME_API_KEY']
        self.base_url = 'https://wakatime.com/api/v1'

    def _create_headers(self, api_key: str) -> dict:
        return {
            # TODO needs refactoring
            'Authorization': 'Basic {}'.format(str(self._encode_api_key(api_key))[2:-1])
        }

    def _encode_api_key(self, api_key: str) -> bytes:
        return base64.b64encode(api_key.encode('utf-8'))

    def get_user(self) -> User:
        res = requests.get(
            '{}/users/current'.format(self.base_url),
            headers=self._create_headers(self.api_key))
        translator = WakatimeUserTranslator(res.json())
        return translator.to_my_user()
