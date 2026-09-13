from typing import Any
import csv
from collections import defaultdict

def read_csv_file(address: str) -> Any:
    """Чтение финансовых операций csv файла"""

    # Dictionary to hold the grouped sums
    grouped_data = defaultdict(float)

    # 1. Read and process the CSV file
    with open(address, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Extract the columns
            last_digits = row["Номер карты"]
            total_spent = row["Сумма операции"]

            # 2. Clean string: remove commas and convert to float
            amount_float = float(total_spent.replace(",", ""))

            # 3. Sum values based on the unique category key
            if amount_float < 0:
                grouped_data[last_digits] += amount_float

    # 4. Transform the result into an array of objects
    result_array = [
        {"last_digits": key, "total_spent": value} for key, value in grouped_data.items()
    ]

    for row in result_array:
        row['cashback'] = abs(row['total_spent'] / 100)
        row['total_spent'] = abs(row['total_spent'])
        row['last_digits'] = row['last_digits'][1:]

    return result_array