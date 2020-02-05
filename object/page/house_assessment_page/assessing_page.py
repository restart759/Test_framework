from object.page.base_page.page_function import *


class AssessingPage(PageFunction):

    def assessing_page(self):
        assessing_tab = '//span[text()="评估确认"]'
        client_name = '//a[text()="张一"]'
        area = '//span[contains(text(),"面积")]/following::input[1]'
        floor = '//span[contains(text(),"所在层")]/following::input[1]'
        room = '//span[text()="居室"]/following::input[1]'
        room_type = '//iframe/following-sibling::div[3]/ul/li[1]'
        elevator = '//span[text()="是否电梯房"]/following::input[1]'
        renovation1 = '//span[text()="装修情况"]/following::input[1]'
        renovation = '//iframe/following-sibling::div[3]/ul/li[1]'
        house_property = '//span[contains(text(),"房产类型")]/following::input[1]'
        property_type = '//iframe/following-sibling::div[3]/ul/li[1]'
        price = '//span[contains(text(),"单价")]/following::input[1]'
        total_price = '//span[contains(text(),"总价")]/following::input[1]'
        source = '//span[contains(text(),"信息来源")]/following::input[1]'
        dttm1 = '//span[contains(text(),"信息挂牌时间")]/following::input[1]'
        dttm = '//iframe/following::tr[1]/following::td[1]'
        add_button = '//button[contains(text(),"添加")]'

        self.driver.find_element_by_xpath(assessing_tab).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(client_name).click()
        self.driver.find_element_by_xpath(area).send_keys('120')
        self.driver.find_element_by_xpath(floor).send_keys('5')
        self.driver.find_element_by_xpath(room).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(room_type).click()
        self.driver.find_element_by_xpath(elevator).click()
        self.driver.find_element_by_xpath(renovation1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(renovation).click()
        self.driver.find_element_by_xpath(house_property).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(property_type).click()
        self.driver.find_element_by_xpath(price).send_keys('12000')
        self.driver.find_element_by_xpath(total_price).send_keys('1650000')
        self.driver.find_element_by_xpath(source).send_keys('链家')
        self.driver.find_element_by_xpath(dttm1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(dttm).click()
        self.driver.find_element_by_xpath(add_button).click()
        time.sleep(1)