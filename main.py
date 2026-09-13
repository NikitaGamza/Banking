import csv
import json

from src.views import process_datetime
from src.file_read import read_csv_file


import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "Banking", "data", "operations.xlsx")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "Banking", "data", "operations.csv")


if __name__ == "__main__":
    input_date = "2026-09-13 14:30:00"
    json_result = process_datetime(input_date)
    json_parsed = json.loads(json_result)
    df = pd.read_csv(PATH_TO_FILE_CSV)

    unique_values = df['Номер карты'].str[1:].unique()
    # Convert each item to a dictionary
    array_of_dicts = [{"last_digits": num_card} for num_card in unique_values]
    json_parsed["cards"] = array_of_dicts
    print(json_parsed)


    # df = pd.read_csv(PATH_TO_FILE_CSV)
    # unique_values = df['Номер карты'].str[1:].unique()
    # Sum 'Сумма операции' where 'Номер карты' equals '*7197'
    # total_sum = df.loc[df['Номер карты'] == '*7197', 'Сумма операции'].sum()
    # print(type(unique_values))
    # print(f"Total Amount: {total_sum}")

    # total_sum = 0
    # with open(PATH_TO_FILE_CSV, mode='r', newline='', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         # Check condition
    #         if row['Номер карты'] == '*7197':
    #             # Convert string value to float or int before adding
    #             total_sum += float(row['Сумма операции'].replace(',', '.'))
    # print(f"Total Amount: {total_sum}")
