#!/usr/bin/python
# -*- coding:utf-8 -*-

from object.baseuse.base_func import BaseFunc
from object.page.base_page.new_thing import NewThing
from object.page.apply_page.search_open_apply import SearchAndOpenApply
import time


class MainSubPage(BaseFunc):
    # 定位二级菜单
    def house_assessment_search(self):
        search = '//span[text()="房屋评估管理"]/following::span[text()="查询"]'
        time.sleep(1)
        self.find_element(search).click()

    def house_assessment_new(self):
        new = '//span[text()="房屋评估管理"]/following::span[text()="新建评估工单"]'

        self.wait_until_visible(new)
        self.find_element(new).click()
        from object.page.base_page.new_thing import NewThing
        return NewThing(self.driver)

    def house_assessment_confirm(self):
        confirm = '//span[text()="房屋评估管理"]/following::span[text()="评估确认"]'

        self.wait_until_visible(confirm)
        self.find_element(confirm).click()
        from object.page.house_assessment_page.assessment_confirm import Confirm
        return Confirm(self.driver)

    def house_assessment_assessing(self):
        assessing = '//span[text()="房屋评估管理"]/following::span[text()="业务确认"][1]'

        self.wait_until_visible(assessing)
        self.find_element(assessing).click()
        from object.page.house_assessment_page.assessing_page import AssessingPage
        return AssessingPage(self.driver)

    def search_apply(self, loan_type):
        search_apply = '//span[contains(text(),"'+loan_type+'")]/following::span[contains(text(),"申请件查询")][1]'
        time.sleep(1)
        self.find_element(search_apply).click()

    def apply_position(self, loan_type, apply_no='', status=''):
        new_apply = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="业务交单"][1]'
        telephone = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="电核"][1]'
        outing = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="外访"][1]'
        basic = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="初审"][1]'
        final = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="终审"][1]'
        confirm = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="业务确认"][1]'
        prepare_assign = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="签约准备"][1]'
        offline_assign = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="线下签约"][1]'
        assign_audit = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="签约审核"][1]'
        assigned = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="材料准备"][1]'

        time.sleep(1)
        if apply_no != '':
            if status == 'NEW':
                self.find_element(new_apply).click()
            elif status == 'TELEPHONE':
                self.find_element(telephone).click()
            elif status == 'OUTING':
                self.find_element(outing).click()
            elif status == 'BASIC':
                self.find_element(basic).click()
            elif status == 'FINAL':
                self.find_element(final).click()
            elif status == 'CONFIRMED':
                self.find_element(confirm).click()
            elif status == 'PREPARE_ASSIGN':
                self.find_element(prepare_assign).click()
            elif status == 'OFFLINE_ASSIGN':
                self.find_element(offline_assign).click()
            elif status == 'ASSIGN_AUDIT':
                self.find_element(assign_audit).click()
            elif status == 'ASSIGNED':
                self.find_element(assigned).click()
            return SearchAndOpenApply(self.driver)
        else:
            self.find_element(new_apply).click()
            return NewThing(self.driver)

    # def new_apply(self, loan_type, apply_no=''):
    #     new_apply = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="业务交单"][1]'
    #     time.sleep(1)
    #     self.find_element(new_apply).click()
    #     if apply_no == '':
    #         return NewThing(self.driver)
    #     else:
    #         return SearchAndOpenApply(self.driver)
    #
    # def telephone(self, loan_type):
    #     telephone = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="电核"][1]'
    #     time.sleep(1)
    #     self.find_element(telephone).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def outing(self, loan_type):
    #     outing = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="外访"][1]'
    #     time.sleep(1)
    #     self.find_element(outing).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def basic(self, loan_type):
    #     basic = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="初审"][1]'
    #     time.sleep(1)
    #     self.find_element(basic).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def final(self, loan_type):
    #     final = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="终审"][1]'
    #     time.sleep(1)
    #     self.find_element(final).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def confirm(self, loan_type):
    #     confirm = '//span[contains(text(),"' + loan_type + '")]/following::span[text()="业务确认"][1]'
    #     time.sleep(1)
    #     self.find_element(confirm).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def prepare_assign(self, loan_type):
    #     prepare_assign = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="签约准备"][1]'
    #     time.sleep(1)
    #     self.find_element(prepare_assign).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def offline_assign(self, loan_type):
    #     offline_assign = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="线下签约"][1]'
    #     time.sleep(1)
    #     self.find_element(offline_assign).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def assign_audit(self, loan_type):
    #     assign_audit = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="签约审核"][1]'
    #     time.sleep(1)
    #     self.find_element(assign_audit).click()
    #     return SearchAndOpenApply(self.driver)
    #
    # def assigned(self, loan_type):
    #     assigned = '//span[contains(text(),"'+loan_type+'")]/following::span[text()="材料准备"][1]'
    #     time.sleep(1)
    #     self.find_element(assigned).click()
    #     return SearchAndOpenApply(self.driver)
