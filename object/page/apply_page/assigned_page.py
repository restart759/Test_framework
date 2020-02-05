from object.baseuse.base_func import *
import pyautogui as pag
import time


class AssignedPage(BaseFunc):

    def assigned_page(self, sub_type, loan_type):
        workspace = '//span[contains(text(),"工作台")]'
        id_card = '//span[text()="身份证正面(打码)"]'
        business_license = '//span[text()="营业执照(打码)"]'
        house = '//span[text()="房产证(打码)"]'
        other_certificate = '//span[text()="他证(打码)"]'
        front_car = '//span[text()="车前照(打码)"]'
        back_car = '//span[text()="车后照(打码)"]'
        nameplate = '//span[text()="铭牌(打码)"]'

        self.wait_until_visible(workspace)
        self.find_element(id_card).click()
        time.sleep(0.5)
        pag.press('printscreen')
        time.sleep(0.5)
        pag.hotkey('ctrl', 'v')
        time.sleep(2)
        self.find_element(business_license).click()
        time.sleep(0.5)
        pag.press('printscreen')
        time.sleep(0.5)
        pag.hotkey('ctrl', 'v')
        time.sleep(2)
        if sub_type == '房抵' or sub_type == '过桥':
            self.find_element(house).click()
            time.sleep(0.5)
            pag.press('printscreen')
            time.sleep(0.5)
            pag.hotkey('ctrl', 'v')
            time.sleep(2)
            if sub_type == '房抵':
                self.find_element(other_certificate).click()
                time.sleep(0.5)
                pag.press('printscreen')
                time.sleep(0.5)
                pag.hotkey('ctrl', 'v')
                time.sleep(2)
        elif loan_type == '车贷信审':
            self.find_element(front_car).click()
            time.sleep(0.5)
            pag.press('printscreen')
            time.sleep(0.5)
            pag.hotkey('ctrl', 'v')
            time.sleep(2)
            self.find_element(back_car).click()
            time.sleep(0.5)
            pag.press('printscreen')
            time.sleep(0.5)
            pag.hotkey('ctrl', 'v')
            time.sleep(2)
            self.find_element(nameplate).click()
            time.sleep(0.5)
            pag.press('printscreen')
            time.sleep(0.5)
            pag.hotkey('ctrl', 'v')
            time.sleep(2)

