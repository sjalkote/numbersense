import unittest

from Player import Player


class TestPlayerCreation(unittest.TestCase):
    def test_invalid_username_corrector(self) -> None:
        assert Player.fix_username("Harry-_-!@$/.,)(*&^\\}{|[1Potter") == ("Harry-_-1Potter", False)

    def test_guest_creation(self) -> None:
        guest_username, is_guest = Player.fix_username("")
        assert is_guest is True
        assert guest_username.startswith('guest')
