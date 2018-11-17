from app.dataaccess.wakatime.api import WakatimeAPIDataSource
from app.domain.model.user import User


class FindCurrentUser:
    def __init__(self, datasource: WakatimeAPIDataSource) -> None:
        self.datasource = datasource

    def run(self) -> User:
        return self.datasource.get_user()
