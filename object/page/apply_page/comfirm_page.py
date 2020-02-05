from object.baseuse.base_func import *
import time


class ConfirmPage(BaseFunc):

    def confirm_page(self, loan_type, sub_type, amount):
        workspace = '//span[contains(text(),"工作台")]'
        credit_amount = '//span[contains(text(),"签约金额")]/following::input[1]'
        mortgagee = '//span[contains(text(),"抵押权人")]/following::input[1]'
        f_mortgagee = '//iframe/following::span[contains(text(),"耿冰杰")]'
        kx_mortgagee = '//iframe/following::span[contains(text(),"江苏应天")]'

        self.wait_until_visible(workspace)
        self.find_element(credit_amount).send_keys(amount)
        if loan_type == '房抵信审':
            self.find_element(mortgagee).click()
            time.sleep(1.5)
            if sub_type == '房抵':
                self.find_element(f_mortgagee).click()
                time.sleep(1)
            elif sub_type == '开心租':
                self.find_element(kx_mortgagee).click()
                time.sleep(1)
