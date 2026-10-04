from src.views import main_info
from src.services import anylize_cashback


# import os

# ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
# PATH_TO_FILE = os.path.join(ROOT_DIR, "Banking", "data", "operations.xlsx")
# PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "Banking", "data", "operations.csv")


if __name__ == "__main__":
    print(main_info("2018-05-20 15:30:01"))
    result_services = anylize_cashback("./data/operations.xlsx", 2018, 3)
    print(result_services)