import csv
import json

from src.views import process_datetime
from src.file_read import read_csv_file


import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PATH_TO_FILE = os.path.join(ROOT_DIR, "Banking", "data", "operations.xlsx")
PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "Banking", "data", "operations.csv")


if __name__ == "__main__":
    input_date = "2026-09-13 14:30:00"
    json_result = process_datetime(input_date)
    json_parsed = json.loads(json_result)


    # Dictionary to hold the grouped sums
    result_array = read_csv_file(PATH_TO_FILE_CSV)

    json_parsed["cards"] = result_array
    print(json_parsed)