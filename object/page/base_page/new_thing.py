#!/usr/bin/python
# -*- coding:utf-8 -*-

from object.baseuse.base_func import BaseFunc
from object.page.base_page.page_function import PageFunction
from object.page.apply_page.new_apply_page import NewApplyPage
from object.page.house_assessment_page.new_assessment_page import NewAssessment
import time
import os


class NewThing(BaseFunc):
    # 新建申请件-新建操作
    def new_apply(self, customer_name, id_no, loan_type, sub_type, client_type):
        sub_type1 = '//label[contains(text(),"车辆质押")]'
        sub_type2 = '//label[contains(text(),"车辆抵押")]'
        sub_type3 = '//label[contains(text(),"车辆让与担保")]'
        sub_type4 = '// label[contains(text(), "过桥")]'
        new_button = '//span[text()=" 业务交单"]/following::button[text()=" 新建申请件"][2]'
        f_new_button = '//span[text()=" 业务交单"]/following::button[text()=" 新建申请件"]'
        company = '//label[contains(text(),"企业客户")]'
        client = '//span[contains(text(),"客户姓名")]/following::input[1]'
        id = '//span[contains(text(),"身份证")]/following::input[1]'
        heshi = '//button[contains(text(),"核实")]'
        new = '//button[contains(text(),"新建申请单")]'
        pop_up_window = '// div[text() = "新建申请件"]'
        applyno = '//div[contains(text(),"借款信息[")]'

        self.wait_until_clickable(new_button)
        if loan_type == '过桥信审' or loan_type == '车贷信审':
            self.find_element(new_button).click()
        elif loan_type == '房抵信审':
            self.find_element(f_new_button).click()

        self.wait_until_visible(pop_up_window)
        if sub_type == '过桥':
            self.find_element(sub_type4).click()
        elif sub_type == '车辆质押':
            self.find_element(sub_type1).click()
        elif sub_type == '车辆抵押':
            self.find_element(sub_type2).click()
        elif sub_type == '车辆让与担保':
            self.find_element(sub_type3).click()

        # 核实客户信息
        if client_type == '企业':
            self.find_element(company).click()
        self.find_element(client).send_keys(customer_name)
        self.find_element(id).send_keys(id_no)
        self.find_element(heshi).click()
        self.wait_until_visible(new)
        self.find_element(new).click()
        self.wait_until_visible(applyno)
        apply_no = self.find_element(applyno).text
        apply = apply_no.split('[')[-1].split(']')[0]
        return apply

    # 新建评估工单-新建操作
    def new_assessment(self):
        new_button = '//button[text()=" 新建评估申请"]'
        upload_button = '//button[contains(text(),"权利人页照片")]'
        customer_name = '//span[contains(text(),"产权人姓名")]/following::input[1]'
        house_property = '//span[contains(text(),"房产类型")]/following::input[1]'
        earth_usage_cert_no = '//span[contains(text(),"房屋所有权证号")]/following::input[1]'
        room = '//span[text()="居室"]/following::input[1]'
        city_code = '//span[text()="省份"]/following::input[1]'
        city_name = '//span[text()="城市"]/following::input[1]'
        district = '//span[text()="区/县"]/following::input[1]'
        detail_address = '//span[contains(text(),"详细地址")]/following::input[1]'
        com_name = '//span[contains(text(),"小区名称")]/following::input[1]'
        submit = '//button[text()="提交"]'

        self.wait_until_visible(new_button)
        self.find_element(new_button).click()
        self.wait_until_visible(upload_button)
        self.find_element(upload_button).click()
        time.sleep(1)
        os.system("C:\\Users\\Administrator\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
        self.wait_until_visible(customer_name)
        # 核实房产证信息
        self.find_element(customer_name).send_keys('张一')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(house_property))
        self.find_element(house_property).clear()
        self.find_element(house_property).send_keys("住宅")
        self.find_element(earth_usage_cert_no).send_keys('十堰房权证茅箭区字第20176637号')
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(room))
        self.find_element(room).clear()
        self.find_element(room).send_keys("一居室")
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(city_code))
        self.find_element(city_code).clear()
        self.find_element(city_code).send_keys("江苏省")
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(city_name))
        self.find_element(city_name).clear()
        self.find_element(city_name).send_keys("连云港市")
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(district))
        self.find_element(district).clear()
        self.find_element(district).send_keys("赣榆区")
        self.find_element(detail_address).send_keys('茅箭区二堰街办堰桥街5号1幢1-2-1')
        self.find_element(com_name).send_keys('吉普三号')
        self.find_element(submit).click()
        return NewAssessment(self.driver)
