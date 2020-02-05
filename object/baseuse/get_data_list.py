from lib.read_excel import *
from config.config import *


def get_data_list(sheet_name):
    if sheet_name == "client_info":
        client_data_list = excel_to_list(os.path.join(data_path, "loan_info.xlsx"), sheet_name)
        return client_data_list
    elif sheet_name == "login_user":
        user_data_list = excel_to_list(os.path.join(data_path, "loan_info.xlsx"), sheet_name)
        return user_data_list
    elif sheet_name == "contact_info":
        contact_data_list = excel_to_list(os.path.join(data_path, "loan_info.xlsx"), sheet_name)
        return contact_data_list
