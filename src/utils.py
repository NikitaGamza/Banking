from datetime import datetime


def get_time_for_greeting(time: str) -> str:
    """Функция возвращает «Доброе утро» / «Добрый день» /
        «Добрый вечер» / «Доброй ночи» в зависимости от текущего времени.
    """
    user_datetime_hour = datetime.now().hour
    if 5 <= user_datetime_hour <= 12:
        return "Доброе утро"
    elif 12 <= user_datetime_hour <= 18:
        return "Добрый день"
    elif 18 <= user_datetime_hour <= 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"