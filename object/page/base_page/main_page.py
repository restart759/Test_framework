#!/usr/bin/python
# -*- coding:utf-8 -*-

from object.baseuse.base_func import *
from object.page.base_page.main_sub_page import MainSubPage


class MainPage(BaseFunc):

    # 定位一级菜单
    def xinshen(self, loan_type):
        loan_type1 = '//span[contains(text(),"'+loan_type+'")]'

        self.driver.refresh()
        self.wait_until_visible(loan_type1)
        if loan_type != '房抵信审':
            self.find_element(loan_type1).click()
        return MainSubPage(self.driver)

    def house_assessment(self):
        house_assessment_tab = '//span[text()="房屋评估管理"]'

        self.driver.refresh()
        self.wait_until_visible(house_assessment_tab)
        self.find_element(house_assessment_tab).click()
        return MainSubPage(self.driver)

