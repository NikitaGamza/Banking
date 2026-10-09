from datetime import datetime

from src.utils import get_time_for_greeting


def test_get_time_for_greeting():
    greeting = get_time_for_greeting()
    possible_values = ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"]
    is_true = greeting in possible_values
    assert is_true == True