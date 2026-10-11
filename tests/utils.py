import pandas as pd

from src.utils import get_data_time, get_path_and_period, get_time_for_greeting


def test_get_time_for_greeting():
    greeting = get_time_for_greeting()
    possible_values = ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"]
    is_true = greeting in possible_values
    assert is_true == True


def test_get_data_time():
    dt = get_data_time("2021-05-20 15:30:01")
    assert dt == ["01.05.2021 15:30:01", "20.05.2021 15:30:01"]


def test_get_path_and_period():
    df = get_path_and_period(
        "./data/operations.xlsx", ["01.12.2021 21:10:01", "02.12.2021 21:10:01"]
    )
    expected_res = pd.DataFrame([7, 9, 11, 13, 15])
    pd.testing.assert_series_equal((df), expected_res, check_names=False)
