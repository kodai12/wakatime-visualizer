import json

from app.application.query import FindCurrentUser
from app.dataaccess.wakatime.api import WakatimeAPIDataSource


def find_current_user_handler(event, context):
    datasource = WakatimeAPIDataSource()
    service = FindCurrentUser(datasource)
    user = service.run()

    body = {
        "name": user.name.value,
        "email": user.email.value
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
