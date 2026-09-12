from src.views import process_datetime


if __name__ == "__main__":
    input_date = "2026-09-13 14:30:00"
    json_result = process_datetime(input_date)
    print(json_result)