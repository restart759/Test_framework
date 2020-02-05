#!/usr/bin/python
# -*- coding:utf-8 -*-

from object.baseuse.base_func import *
import os
import time


class PageFunction(BaseFunc):
    workspace = '//span[contains(text(),"工作台")]'
    close_tab = '//div[@class="z-tab-button"]//following::i[@class="z-icon-times z-tab-icon"][last()]'
    new_thing = '//button[contains(text(),"新建")]'
    submit = '//button[contains(text(),"提交")]'
    submit0 = '//i[@class="z-icon-check"]'
    submit1 = '//button[contains(text(),"初审通过")]'
    submit2 = '//button[contains(text(),"线上发标")]'
    waiting = '//div[@class="z-loading-indicator"]'
    confirm = '//button[text()="是"]'
    success_confirm = '//button[text()="确认"]'
    go_back = '//button[contains(text(),"退回")]'
    upload_file_count = '//button[text()=" 附件打包下载"]/following::tr[4]//child::li'
    upload_file_type = '//button[text()=" 附件打包下载"]/following::tr[4]//child::li[{}]'
    choose_file = '//button[contains(text(),"请选择附件")]'
    confirm_button = '//button[@class="z-messagebox-button btn"]'

    # 退出登录
    def logout(self):
        logout_button = '//a[text()="退出"]'
        self.driver.find_element_by_xpath(logout_button).click()

    # 关闭标签页
    def close(self):
        self.wait_until_visible(self.workspace)
        self.find_element(self.close_tab).click()
        from object.page.base_page.main_page import MainPage
        return MainPage(self.driver)

    # 提交
    def submit_apply(self, status):
        if status in ('NEW', 'TELEPHONE', 'OUTING', 'FINAL'):
            self.find_element(self.submit).click()
        elif status == 'BASIC':
            self.find_element(self.submit1).click()
        elif status in ('CONFIRMED', 'PREPARE_ASSIGN', 'OFFLINE_ASSIGN', 'ASSIGN_AUDIT'):
            self.find_element(self.submit0).click()
        elif status == 'ASSIGNED':
            self.find_element(self.submit2).click()
        self.wait_until_visible(self.confirm_button)
        self.find_element(self.confirm_button).click()
        self.wait_until_visible(self.success_confirm)

    # 退回
    def go_back_apply(self):
        self.find_element(self.go_back).click()
        return PageFunction(self.driver)

    # 上传附件
    def upload_picture(self):
        for i in range(1, len(self.find_elements(self.upload_file_count))+1):
            self.find_element(self.upload_file_type.format(i)).click()
            time.sleep(1.5)
            self.find_element(self.choose_file).click()
            time.sleep(2)
            os.system("C:\\Users\\Administrator\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
            time.sleep(2)






