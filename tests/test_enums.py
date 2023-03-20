import unittest

from Enums import QuizType


class TestEnums(unittest.TestCase):
    def test_enum_str_conversion(self) -> None:
        assert str(QuizType.EASY) == "Easy"
        assert str(QuizType.NORMAL) == "Normal"
        assert str(QuizType.HARD) == "Hard"
        assert str(QuizType.QUICK) == "Quick"
