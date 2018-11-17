import os
from app.dataaccess.wakatime.auth import WakatimeAuthDataSource

def get_auth_user_handler():
    datasource = WakatimeAuthDataSource(
        client_id=os.environ['WAKATIME_CLIENT_ID'],
        client_secret=os.environ['WAKATIME_SECRET'])
    url = datasource.get_url()
    print('**** Visit this url in your browser ****'.format(url=url))
    print('*' * 80)
    print(url)
    print('*' * 80)
    print('**** After clicking Authorize, paste code here and press Enter ****')
    code = input('Enter code from url: ')
    session = datasource.get_session(code=code)
    user = datasource.get_user(session=session)
    print('Authenticated via OAuth as {0}'.format(user['data']['email']))

