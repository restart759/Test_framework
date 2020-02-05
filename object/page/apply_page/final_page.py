from object.baseuse.base_func import *
import time


class FinalPage(BaseFunc):

    def final_page(self, loan_type, sub_type, channel, amount):
        workspace = '//span[contains(text(),"工作台")]'
        choose_channel = '//span[contains(text(),"渠道")]/following::input[1]'
        online = '//iframe/following::span[text()="互联网金融"]'
        offline = '//iframe/following::span[text()="持牌机构"]'
        credit_amount = '//span[contains(text(),"授信金额")]/following::input[1]'
        options = '//span[contains(text(),"审核意见")]/following::textarea[1]'
        options1 = '//span[contains(text(),"审核意见")]/following::textarea[2]'
        representative = '//span[contains(text(),"代持人")]/following::input[1]'
        contract_amount = '//span[contains(text(),"合同金额")]/following::input[1]'
        options2 = '//span[contains(text(),"处理意见")]/following::input[1]'
        options3 = '//span[contains(text(),"备注")]/following::textarea[1]'

        self.wait_until_visible(workspace)
        self.find_element(choose_channel).click()
        time.sleep(1)
        if channel == '线下':
            self.find_element(offline).click()
        else:
            self.find_element(online).click()

        if loan_type == '车贷信审':
            if sub_type != '车辆质押':
                self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(representative))
                self.find_element(representative).send_keys('耿冰杰')
            self.find_element(contract_amount).send_keys(amount)
            self.find_element(options2).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(options2))
            self.find_element(options2).send_keys('通过')
            time.sleep(1)
            self.find_element(options3).send_keys('1')
        else:
            self.find_element(credit_amount).send_keys(amount)
            self.find_element(options).send_keys('1')
            self.find_element(options1).send_keys('1')
