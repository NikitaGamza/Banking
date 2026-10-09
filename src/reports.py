from datetime import datetime, timedelta
from typing import Optional

from pandas import DataFrame
import pandas as pd

from pathlib import Path

def spending_by_category(transactions: DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    transaction_category = []

    dt = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    dt = datetime.strptime(dt, "%d.%m.%Y %H:%M:%S")
    if date:
        dt = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    dt_delta = dt - timedelta(days=90)

    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    filtered_df = transactions[
        (transactions["Дата операции"] >= dt_delta) &
        (transactions["Дата операции"] <= dt)
        ]

    for index, row in filtered_df.iterrows():
        if row['Категория'] == category:
            transaction = {
                "date": f"{row['Дата платежа']}",
                "amount": f"{row['Сумма операции']}",
                "category": f"{row['Категория']}",
                "description": f"{row['Описание']}",
            }
            transaction_category.append(transaction)

    transaction_category = pd.DataFrame(transaction_category)
    filepath = Path("./data/out.csv")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    transaction_category.to_csv(filepath)
    return transaction_category