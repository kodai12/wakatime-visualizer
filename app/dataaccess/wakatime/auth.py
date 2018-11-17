import hashlib
import os
from rauth import OAuth2Service


class WakatimeAuthDataSource:
    def __init__(self,
                 client_id: str,
                 client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = 'https://wakatime.com/oauth/test'

    def _get_service(self):
        return OAuth2Service(
            client_id=self.client_id,
            client_secret=self.client_secret,
            name='wakatime',
            authorize_url='https://wakatime.com/oauth/authorize',
            access_token_url='https://wakatime.com/oauth/token',
            base_url='https://wakatime.com/api/v1/')

    def _get_state(self):
        return hashlib.sha1(os.urandom(40)).hexdigest()

    def _get_params(self):
        return {'scope': 'email,read_stats',
                       'response_type': 'code',
                       'state': self._get_state,
                       'redirect_uri': self.redirect_uri}

    def get_url(self):
        service = self._get_service()
        params = self._get_params()
        return service.get_authorize_url(**params)


    def get_session(self, code: str):
        service = self._get_service()
        headers = {'Accept': 'application/x-www-form-urlencoded'}
        print('Getting an access token...')
        return service.get_auth_session(headers=headers,
                                        data={'code': code,
                                              'grant_type': 'authorization_code',
                                              'redirect_uri': self.redirect_uri})

    def get_user(self, session: str):
        return session.get('users/current').json()
