from object.baseuse.base_func import *
import time


class TelephonePage(BaseFunc):

    def telephone_page(self, sub_type):
        workspace = '//span[contains(text(),"工作台")]'
        remarks = '//span[contains(text(),"电核备注")]/following::textarea'
        remarks1 = '//span[contains(text(),"电核备注")]/following::textarea[{}]'
        gq_remarks = '//span[text()="电核备注"]/following::input[1]'
        outing_stuff = '//span[contains(text(),"外访人员")]/following::input[1]'
        outing_stuff1 = '//iframe/following::span[contains(text(),"admin")]'
        outing_time = '//span[contains(text(),"约定外访时间")]/following::input[1]'
        outing_time1 = '//iframe/following::tbody/tr/td[1]'
        province = '//button[contains(text(),"住宅1")]/following::input[1]'
        province1 = '//iframe/following::span[contains(text(),"上海市")]'
        city = '//button[contains(text(),"住宅1")]/following::input[2]'
        city1 = '//iframe/following::span[contains(text(),"上海市")]'
        area = '//button[contains(text(),"住宅1")]/following::input[3]'
        area1 = '//iframe/following::span[contains(text(),"杨浦区")]'
        address = '//button[contains(text(),"住宅1")]/following::input[4]'

        self.wait_until_visible(workspace)
        for i in range(1, len(self.find_elements(remarks))+1):
            self.find_element(remarks1.format(i)).send_keys('111')
        if sub_type == '房抵' or sub_type == '信用' or sub_type == '过桥':
            self.find_element(outing_stuff).click()
            self.wait_until_visible(outing_stuff1)
            self.find_element(outing_stuff1).click()
            time.sleep(1)
            self.find_element(outing_time).click()
            self.wait_until_visible(outing_time1)
            self.find_element(outing_time1).click()
            time.sleep(1)
            if sub_type == '过桥':
                self.find_element(gq_remarks).send_keys('111')
            if sub_type == '房抵':
                self.find_element(province).click()
                self.wait_until_visible(province1)
                self.find_element(province1).click()
                time.sleep(1)
                self.find_element(city).click()
                self.wait_until_visible(city1)
                self.find_element(city1).click()
                time.sleep(1)
                self.find_element(area).click()
                self.wait_until_visible(area1)
                self.find_element(area1).click()
                time.sleep(1)
                self.find_element(address).send_keys('武东路198号')
