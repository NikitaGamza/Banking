from datetime import datetime
import json


def parse_datetime(dt_str: str) -> datetime:
    """Конвертирует строку в объект datetime."""
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")


def get_session_info(dt: datetime) -> dict:
    """Вычисляет календарные параметры для заданной даты."""
    # Порядковый номер дня в году (1-366)
    hour = int(dt.strftime("%H"))
    if 6 <= hour < 12:
        greet = 'Доброе утро'
    elif 12 <= hour < 18:
        greet = 'Добрый день'
    elif 18 <= hour < 24:
        greet = 'Добрый вечер'
    else:
        greet = 'Доброй ночи'

    return {
        "greeting": greet,
    }


def process_datetime(dt_str: str) -> str:
    """Главная функция: принимает строку, возвращает JSON-ответ."""
    try:
        dt_obj = parse_datetime(dt_str)
        data = get_session_info(dt_obj)
        # Возвращаем JSON-строку с красивыми отступами и поддержкой utf-8
        return json.dumps(data, indent=4, ensure_ascii=False)
    except ValueError as e:
        return json.dumps(
            {"error": "Неверный формат даты. Используйте YYYY-MM-DD HH:MM:SS"},
            ensure_ascii=False,
        )