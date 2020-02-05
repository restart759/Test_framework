from object.page.base_page.login_page import Login
from object.page.base_page.main_page import MainPage
from object.page.base_page.page_function import PageFunction
import unittest
from selenium import webdriver
from object.baseuse.get_apply_info import *
from object.baseuse.get_data_list import get_data_list


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://115.159.95.162:8182/credit/zuls/home.zul')

    # def test_search_apply(self):
    #     apply_no = 'AT201912230001'
    #     # 获取主借人信息/合同数据要求
    #     data_list = get_data_list("client_info")
    #     contact_data_list = ''
    #     for data in data_list:
    #         client_type = data.get('client_type')
    #         contact_no = data.get('contact_no')
    #         amount = int(data.get('amount'))
    #         channel = data.get('channel')
    #         count = int(data.get('count'))
    #         # 获取申请件类型及状态
    #         sub_type = get_apply_info(apply_no)['sub_type']
    #         loan_type = get_apply_info(apply_no)['loan_type']
    #         status = get_apply_info(apply_no)['status']
    #         # 获取互金线上签约与用户登陆账号
    #         login_name_list = get_login_name(apply_no)
    #         # 获取共签人列表
    #         if contact_no != 0:
    #             contact_data_list = get_data_list("contact_info")
    #
    #         Login(self.driver).login_page('admin', '111111').xinshen(loan_type).apply_position(loan_type, apply_no, status).\
    #             search_and_open_apply(apply_no, status, loan_type, sub_type, amount, client_type, contact_no, channel,
    #                                   count, login_name_list, contact_data_list)

    def test_new_apply(self):
        # 获取主借人信息/合同数据要求
        data_list = get_data_list("client_info")
        contact_data_list = ''
        for data in data_list:
            customer_name = data.get('customer_name')
            id_no = data.get('id_no')
            client_type = data.get('client_type')
            loan_type = data.get('loan_type')
            sub_type = data.get('sub_type')
            contact_no = int(data.get('contact_no'))
            amount = int(data.get('amount'))
            channel = data.get('channel')
            count = int(data.get('count'))

            apply_no = 'AT202001120004'
            # apply_no = Login(self.driver).login_page('limin', '111111').xinshen(loan_type).apply_position(loan_type).\
            #     new_apply(customer_name, id_no, loan_type, sub_type, client_type)
            # PageFunction(self.driver).logout()
            Login(self.driver).login_page('admin', '111111')
            # 获取申请件状态
            status = get_apply_info(apply_no)['status']
            loan_type = get_apply_info(apply_no)['loan_type']
            sub_type = get_apply_info(apply_no)['sub_type']
            print(status)
            # 获取互金线上签约与用户登陆账号
            login_name_list = get_login_name(apply_no)
            # 获取共签人列表
            if contact_no != 0:
                contact_data_list = get_data_list("contact_info")

            while status != 'COMPLETE':
                MainPage(self.driver).xinshen(loan_type).\
                    apply_position(loan_type, apply_no, status).\
                    search_and_open_apply(apply_no, status, loan_type, sub_type, amount, client_type, contact_no,
                                          channel, count, login_name_list, contact_data_list).submit_apply(status)
                status = get_apply_info(apply_no)['status']

    # def test_house_assessment(self):
    #     Login(self.driver).login_page('admin', '111111').house_assessment().house_assessment_new().new_assessment().\
    #         assessment_new()


if __name__ == '__main__':
    unittest.main()
