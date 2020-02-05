from object.baseuse.base_func import *
import time


class PrepareAssignPage(BaseFunc):

    def prepare_assign_page(self, sub_type):
        workspace = '//span[contains(text(),"工作台")]'
        generate_contract = '//i[@class="z-icon-plus-square"]'
        car_id = '//span[text()="新车牌号"]/following::input[1]'
        choose_lender = '//span[contains(text(),"出借人")]/following::input[1]'
        kx_lender = '//iframe/following::span[contains(text(),"江苏应天")]'
        lender = '//iframe/following::span[contains(text(),"耿冰杰")]'
        submit = '//button[contains(text(),"提交")]'
        confirm_button = '//button[@class="z-messagebox-button btn"]'
        contract = '//div[text()="合同文本"]'

        self.wait_until_visible(workspace)
        self.find_element(generate_contract).click()
        time.sleep(1)
        if sub_type == '车辆让与担保':
            self.find_element(car_id).send_keys('赣C11111')
        self.find_element(choose_lender).click()
        time.sleep(1)
        if sub_type == '开心租':
            self.find_element(kx_lender).click()
            time.sleep(1)
        else:
            self.find_element(lender).click()
            time.sleep(1)
        self.find_element(submit).click()
        self.wait_until_visible(confirm_button)
        self.find_element(confirm_button).click()
        self.wait_until_visible(contract)
