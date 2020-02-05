from object.baseuse.base_func import *
import time


class NewAssessment(BaseFunc):

    def assessment_new(self):
        area = '//span[contains(text(),"面积")]/following::input[1]'
        floor = '//span[contains(text(),"所在层")]/following::input[1]'
        total_floor = '//span[contains(text(),"总楼层")]/following::input[1]'
        renovation1 = '//span[text()="装修情况"]/following::input[1]'
        renovation = '//iframe/following::span[contains(text(),"简装")]'
        decoration_age1 = '//span[text()="装修年限"]/following::input[1]'
        decoration_age = '//iframe/following::span[contains(text(),"1年")]'
        is_actual_address = '//span[contains(text(),"是否为实际地址")]/following::input[1]'

        self.driver.find_element_by_xpath(area).send_keys('120')
        self.driver.find_element_by_xpath(floor).send_keys('5')
        self.driver.find_element_by_xpath(total_floor).send_keys('6')
        self.driver.find_element_by_xpath(renovation1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(renovation).click()
        self.driver.find_element_by_xpath(decoration_age1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(decoration_age).click()
        self.driver.find_element_by_xpath(is_actual_address).click()
        time.sleep(1)
