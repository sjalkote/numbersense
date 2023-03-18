import unittest

from Player import Player


class TestPlayerCreation(unittest.TestCase):
    def test_invalid_username_corrector(self) -> None:
        assert Player.fix_username("Harry-_-!@$/.,)(*&^\\}{|[1Potter") == "Harry-_-1Potter"
