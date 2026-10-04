from datetime import datetime
import json
from typing import Dict, Any
from src.utils import (
    get_time_for_greeting,
    get_data_time,
    get_path_and_period,
    get_card_with_spend,
    get_top_transactions,
    get_currency,
    get_stock
)


def main_info(date_time: str) -> Dict[str, Any]:
    """главная функция, принимающую на вход строку с датой и временем в формате
        YYYY-MM-DD HH:MM:SS (2018-05-20 15:30:01) и возвращающую json-ответ
    """
    # Сраз экселя на определённый диапазон
    time_period = get_data_time(date_time)
    sorted_df = get_path_and_period("./data/operations.xlsx", time_period)

    # 1. Приветствие
    greeting = get_time_for_greeting()

    # 2. Данные по каждой карте
    cards = get_card_with_spend(sorted_df)

    # 3. Топ 5 транзанкций
    top_transactions = get_top_transactions(sorted_df, 5)

    # 4. Курс валют
    currency_rates = get_currency("./data/user_settings.json")

    # 5. Стоимость акций из S&P500
    stock_prices = get_stock("./data/user_settings.json")

    data = {
        "greeting": greeting,
        # "cards": cards
        # "top_transactions": top_transactions
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }

    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    return json_data




# def parse_datetime(dt_str: str) -> datetime:
#     """Конвертирует строку в объект datetime."""
#     return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
#
#
# def get_session_info(dt: datetime) -> dict:
#     """Вычисляет календарные параметры для заданной даты."""
#     # Порядковый номер дня в году (1-366)
#     hour = int(dt.strftime("%H"))
#     if 6 <= hour < 12:
#         greet = 'Доброе утро'
#     elif 12 <= hour < 18:
#         greet = 'Добрый день'
#     elif 18 <= hour < 24:
#         greet = 'Добрый вечер'
#     else:
#         greet = 'Доброй ночи'
#
#     return {
#         "greeting": greet,
#     }
#
#
# def process_datetime(dt_str: str) -> str:
#     """Главная функция: принимает строку, возвращает JSON-ответ."""
#     try:
#         dt_obj = parse_datetime(dt_str)
#         data = get_session_info(dt_obj)
#         # Возвращаем JSON-строку с красивыми отступами и поддержкой utf-8
#         return json.dumps(data, indent=4, ensure_ascii=False)
#     except ValueError as e:
#         return json.dumps(
#             {"error": "Неверный формат даты. Используйте YYYY-MM-DD HH:MM:SS"},
#             ensure_ascii=False,
#         )