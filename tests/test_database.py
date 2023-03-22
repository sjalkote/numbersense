import datetime
import unittest

import utils
import os


# TODO: move to pytest
class TestDatabase(unittest.TestCase):
    # @pytest.mark.dependency
    def test_create_default_database(self) -> None:
        # Remove database file if it already exists
        if os.path.exists(utils.DB_FILENAME):
            os.remove(utils.DB_FILENAME)

        utils.create_default_db()

        assert os.path.exists(utils.DB_FILENAME)
        assert utils.get_users_table_from_db() == []

    def test_add_user_to_database(self) -> None:
        self.test_create_default_database()
        username: str = "Harry Potter"
        password: str = "amogus"
        current_date: datetime.date = datetime.date.today()

        new_row: tuple = utils.add_user_to_db(username, password, current_date)

        assert username in new_row
        assert password in new_row
        assert current_date.strftime(utils.DB_DATE_FORMAT) in new_row
