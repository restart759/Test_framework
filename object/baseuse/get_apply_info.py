from config.config import *
from lib.db import DB
import string
import random


def get_apply_info(apply_no):
    apply_info_key = ['sub_type', 'loan_type', 'status']
    apply_info_list = []
    apply_info = DB().check_apply_status(apply_no)
    if apply_info[0] is not None:
        st = sub_type[apply_info[0]]
        apply_info_list.append(st)
        lt = loan_type[apply_info[1]]
        apply_info_list.append(lt)
        status = apply_info[2]
        apply_info_list.append(status)
    else:
        if apply_info[1] == 'DY':
            apply_info_list.append('')
        else:
            st = sub_type[apply_info[1]]
            apply_info_list.append(st)
        lt = loan_type[apply_info[1]]
        apply_info_list.append(lt)
        status = apply_info[2]
        apply_info_list.append(status)
    apply_info_dic = dict(zip(apply_info_key, apply_info_list))
    return apply_info_dic


def get_login_name(apply_no):
    login_name_list = DB().check_login_name(apply_no)
    return login_name_list


def insert_outing_pic(apply_no):
    table_id_list = []
    for i in range(3):
        table_id = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(32))
        table_id_list.append(table_id)
    table_key = DB().search_outing_pic_key(apply_no)
    DB().insert_outing_pic(table_id_list, table_key)

