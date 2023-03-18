from enum import Enum, unique


@unique  # Prevents overlap (Cannot be both EASY and HARD simultaneously)
class QuizType(Enum):
    """Defines the different types of quizzes available"""
    def __str__(self):
        return str(self.value)

    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    QUICK = "Quick"
    TWO_PLAYER_VS = "Two Player (v.s.)"
