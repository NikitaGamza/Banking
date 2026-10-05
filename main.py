from src.views import main_info
from src.services import anylize_cashback
from src.reports import spending_by_category
import pandas as pd

# import os

# ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
# PATH_TO_FILE = os.path.join(ROOT_DIR, "Banking", "data", "operations.xlsx")
# PATH_TO_FILE_CSV = os.path.join(ROOT_DIR, "Banking", "data", "operations.csv")


if __name__ == "__main__":
    data_request = "2018-05-20 15:30:01"
    result_view = main_info(data_request)
    print(result_view)

    # result_services = anylize_cashback("./data/operations.xlsx", 2018, 3)
    # print(result_services)

    # df = pd.read_excel('./data/operations.xlsx', sheet_name="Отчет по операциям")
    # result_report = spending_by_category(df, 'Ж/д билеты', "2019-04-10")
    # print(result_report)