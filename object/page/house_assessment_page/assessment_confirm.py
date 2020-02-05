from object.page.base_page.page_function import *


class Confirm(PageFunction):

    def confirm(self):
        confirm_tab = '//span[text()="评估确认"]/following::span[text()="业务确认"][1]'
        client_name = '//a[text()="张一"]'
        trans_date1 = '//span[contains(text(),"可上市交易时间")]/following::input[1]'
        trans_date = '//iframe/following::tr[1]/following::td[1]'
        area_age_from1 = '//span[contains(text(),"土地年限")]/following::input[1]'
        area_age_from = '//iframe/following::tr[1]/following::td[1]'
        area_age_to1 = '//span[contains(text(),"土地年限")]/following::input[2]'
        area_age_to = '//iframe/following::tr[2]/following::td[4]'
        area_property1 = '//span[contains(text(),"土地性质")]/following::input[1]'
        area_property = '//iframe/following-sibling::div[3]/ul/li[1]'
        build_time1 = '//span[contains(text(),"建成年代")]/following::input[1]'
        build_time = '//iframe/following::tr[1]/following::td[1]'
        direction1 = '//span[contains(text(),"朝向")]/following::input[1]'
        direction = '//iframe/following-sibling::div[3]/ul/li[1]'
        parking_price = '//span[contains(text(),"车位价格")]/following::input[1]'

        self.house_assessment()
        self.driver.find_element_by_xpath(confirm_tab).click()
        self.driver.find_element_by_xpath(client_name).click()
        self.driver.find_element_by_xpath(trans_date1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(trans_date).click()
        self.driver.find_element_by_xpath(area_age_from1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(area_age_from).click()
        self.driver.find_element_by_xpath(area_age_to1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(area_age_to).click()
        self.driver.find_element_by_xpath(area_property1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(area_property).click()
        self.driver.find_element_by_xpath(build_time1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(build_time).click()
        self.driver.find_element_by_xpath(direction1).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(direction).click()
        self.driver.find_element_by_xpath(parking_price).send_keys('150000')
        # 上传附件
        self.upload_file()
