import unittest
from Player import *

class TestPlayer(unittest.TestCase):
    def test_create_player_instance(self):
        player1: Player = Player("Harry Potter", QuizType.EASY, "password")