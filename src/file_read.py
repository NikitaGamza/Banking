from typing import Any
import csv


def read_csv_file(address: str) -> Any:
    """Чтение финансовых операций csv файла"""
    transactions = []
    try:
        with open(address, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(dict(row))
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"
    return transactions