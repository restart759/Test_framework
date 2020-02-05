from object.baseuse.base_func import BaseFunc
import time
from object.page.apply_page.new_apply_page import NewApplyPage
from object.page.apply_page.telephone_page import TelephonePage
from object.page.apply_page.outing_page import OutingPage
from object.page.apply_page.basic_page import BasicPage
from object.page.apply_page.final_page import FinalPage
from object.page.apply_page.comfirm_page import ConfirmPage
from object.page.apply_page.prepare_assign_page import PrepareAssignPage
from object.page.apply_page.offline_assign_page import OfflineAssignPage
from object.page.apply_page.assign_audit_page import AssignAuditPage
from object.page.apply_page.assigned_page import AssignedPage


class SearchAndOpenApply(BaseFunc):

    def search_and_open_apply(self, apply_no, status, loan_type='', sub_type='', amount='', client_type='',
                              contact_no='', channel='', count='', login_name_list='', contact_data_list=''):
        f_search_input = '//tbody/following::input[@placeholder="输入申请件编号/客户姓名/证件号码"]'
        search_input = '//tbody/following::input[@placeholder="输入申请件编号/客户姓名/证件号码"][2]'
        f_search_button = '//tbody/following::button[text()=" 查询"]'
        search_button = '//tbody/following::button[text()=" 查询"][2]'
        f_click_apply_no = '//tbody/following::button[text()=" 查询"]//following::a[1]'
        click_apply_no = '//tbody/following::button[text()=" 查询"][2]//following::a[1]'

        time.sleep(4)
        if len(self.find_elements(f_search_input)) > 1:
            self.find_element(search_input).send_keys(apply_no)
            self.find_element(search_button).click()
            time.sleep(3)
            self.find_element(click_apply_no).click()
        elif len(self.find_elements(f_search_input)) == 1:
            self.find_element(f_search_input).send_keys(apply_no)
            self.find_element(f_search_button).click()
            time.sleep(3)
            self.find_element(f_click_apply_no).click()

        if status == 'NEW':
            NewApplyPage(self.driver).new_apply_page(loan_type, sub_type, amount, client_type, contact_no,
                                                     contact_data_list)
        elif status == 'TELEPHONE':
            TelephonePage(self.driver).telephone_page(sub_type)
        elif status == 'OUTING':
            OutingPage(self.driver).outing_page(loan_type, apply_no)
        elif status == 'BASIC':
            BasicPage(self.driver).basic_page(loan_type, sub_type, amount, apply_no)
        elif status == 'FINAL':
            FinalPage(self.driver).final_page(loan_type, sub_type, channel, amount)
        elif status == 'CONFIRMED':
            ConfirmPage(self.driver).confirm_page(loan_type, sub_type, amount)
        elif status == 'PREPARE_ASSIGN':
            PrepareAssignPage(self.driver).prepare_assign_page(sub_type)
        elif status == 'OFFLINE_ASSIGN':
            OfflineAssignPage(self.driver).offline_assign_page()
        elif status == 'ASSIGN_AUDIT':
            AssignAuditPage(self.driver).assign_audit_page(channel, amount, count, login_name_list)
        elif status == 'ASSIGNED':
            AssignedPage(self.driver).assigned_page(sub_type, loan_type)
        from object.page.base_page.page_function import PageFunction
        return PageFunction(self.driver)
