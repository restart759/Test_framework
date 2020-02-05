from object.baseuse.base_func import *
import time
from lib.db import DB


class BasicPage(BaseFunc):

    def basic_page(self, loan_type, sub_type, amount, apply_no):
        workspace = '//span[contains(text(),"工作台")]'
        credit = '//span[text()="征信情况"]/following::input[1]'
        loans = '//span[contains(text(),"负债情况")]/following::input[1]'
        other_loans = '//span[contains(text(),"其他负债")]/following::input[1]'
        options = '//span[contains(text(),"审批意见")]/following::textarea[1]'
        options1 = '//span[contains(text(),"审批意见")]/following::textarea[2]'
        loan_amount = '//span[contains(text(),"授信金额")]/following::input[1]'
        percentage = '//span[contains(text(),"授信成数")]/following::input[1]'
        rent_amount = '//span[contains(text(),"租金")]/following::input[1]'
        source = '//span[contains(text(),"还款来源")]/following::input[1]'
        approval_amount = '//span[contains(text(),"审批金额")]/following::input[1]'
        options2 = '//span[text()="处理意见"]/following::input[1]'

        self.wait_until_visible(workspace)
        DB().update_basic_credit(apply_no)
        if loan_type == '房抵信审' or loan_type == '过桥信审':
            self.find_element(loan_amount).send_keys(amount)
            if sub_type == '信用' or loan_type == '房抵信审':
                self.find_element(percentage).send_keys('1')
                if sub_type == '开心租':
                    self.find_element(rent_amount).send_keys('1000')
            elif sub_type == '过桥':
                self.find_element(percentage).send_keys('0.6')
            if sub_type == '信用' or sub_type == '过桥':
                self.find_element(source).send_keys('1111111')
        else:
            self.find_element(approval_amount).send_keys(amount)
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(options2))
            self.find_element(options2).send_keys('通过')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(credit))
        self.find_element(credit).send_keys('优')
        self.find_element(loans).click()
        self.find_element(other_loans).send_keys('1')
        self.find_element(options).send_keys('1')
        self.find_element(options1).send_keys('1')
