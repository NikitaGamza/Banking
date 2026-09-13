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
    json_parsed["cards"] = unique_values
    print(json_parsed)
