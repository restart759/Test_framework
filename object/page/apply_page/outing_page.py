# from object.baseuse.base_func import BaseFunc
from object.page.base_page.page_function import *
from object.baseuse.get_apply_info import insert_outing_pic


class OutingPage(BaseFunc):

    def outing_page(self, loan_type, apply_no):
        workspace = '//span[contains(text(),"工作台")]'
        family = '//span[contains(text(),"家庭情况")]/following::textarea[1]'
        company = '//span[contains(text(),"企业情况")]/following::textarea[1]'
        loans = '//span[contains(text(),"负债情况")]/following::textarea[1]'
        opinions = '//span[contains(text(),"内部意见")]/following::textarea[1]'
        outing_price = '//span[contains(text(),"外访价格")]/following::a[text()="编辑"]'
        outing_price1 = '//span[contains(text(),"外访价格")]/following::a[text()="编辑"][{}]'
        outing_price_info = '//div[contains(text(),"外访价格信息")]'
        price = '//span[contains(text(),"单价")]/following::input[1]'
        total_price = '//span[contains(text(),"总价")]/following::input[1]'
        plus_button = '//i[@class="z-icon-plus"]'
        plus_info = '//div[contains(text(),"添加中介评估信息")]'
        guarantee = '//span[contains(text(),"押品地址")]/following::input[1]'
        guarantee1 = '//iframe/following::div[text()="请选择"]/following::tbody[1]/tr[{}]'
        company_name = '//span[contains(text(),"公司名称")]/following::input[1]'
        save = '//button[contains(text(),"保存")]'

        self.wait_until_visible(workspace)
        self.find_element(family).send_keys('111')
        self.find_element(company).send_keys('111')
        self.find_element(loans).send_keys('111')
        self.find_element(opinions).send_keys('111')
        if loan_type == '房抵信审':
            house_count = len(self.find_elements(outing_price))
            for i in range(1, house_count+1):
                self.find_element(outing_price1.format(i)).click()
                self.wait_until_visible(outing_price_info)
                self.find_element(price).send_keys('100000')
                self.find_element(total_price).send_keys('1000')
                self.find_element(save).click()
                time.sleep(1)

                self.find_element(plus_button).click()
                self.wait_until_visible(plus_info)
                self.find_element(guarantee).click()
                self.wait_until_visible(guarantee1.format(i))
                self.find_element(guarantee1.format(i)).click()
                time.sleep(1)
                self.find_element(company_name).send_keys('111')
                self.find_element(price).send_keys('100000')
                self.find_element(total_price).send_keys('1000')
                self.find_element(save).click()
                time.sleep(1)
            insert_outing_pic(apply_no)
        if loan_type == '过桥信审':
            PageFunction(self.driver).upload_picture()

