from datetime import datetime

from src.utils import get_time_for_greeting


def test_get_time_for_greeting():
    greeting_1 = get_time_for_greeting()
    greeting_2 = get_time_for_greeting()
    assert greeting_1 == greeting_2