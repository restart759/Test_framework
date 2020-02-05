from object.baseuse.base_func import BaseFunc
import time


class AssignAuditPage(BaseFunc):

    def assign_audit_page(self, channel, amount, count, login_name_list):
        self.assign_audit(channel, amount, count)
        self.hujin_assign(login_name_list)

    def assign_audit(self, channel, amount, count):
        workspace = '//span[contains(text(),"工作台")]'
        split_contract = '//button[contains(text(),"拆分合同")]'
        out_window = '//div[text()="拆分合同"]'
        have_contact = '//label[text()="首款批"]'
        delete_button = '//div[text()="拆分合同"]/following::i[@class="z-icon-trash"][{}]'
        split_amount = '//div[text()="拆分合同"]/following::input[@class="z-doublebox"][{}]'
        plus_button = '//div[text()="拆分合同"]/following::i[@class="z-icon-plus"][{}]'
        final_payment = '//label[text()="尾款批"]'
        submit = '//i[@class="z-icon-close"]//following::button'
        confirm = '//button[@class="z-messagebox-button btn"]'
        online_sign_button = '//button[text()="通知线上签约"]'
        online_sign_button1 = '//div[contains(text(),"S{}")]//div[1]//button[text()="通知线上签约"]'
        sign_confirm = '//button[text()="是"]'
        sign_confirm1 = '//button[text()="确认"]'

        self.wait_until_visible(workspace)
        if count != 1:
            contract_amount = int(amount/count)
            self.find_element(split_contract).click()
            self.wait_until_visible(out_window)
            if len(self.find_elements(have_contact)) > 1 and len(self.find_elements(have_contact)) == count:
                print('进入第一个if')
                for i in range(1, count+1):
                    print('---------------------')
                    self.find_element(split_amount.format(i)).send_keys(contract_amount)
            elif len(self.find_elements(have_contact)) > 1 and len(self.find_elements(have_contact)) > count:
                d_value = len(self.find_elements(have_contact)) - count
                print('进入第二个if,差值为:' + str(d_value))
                for i in range(1, d_value+1):
                    print('删除')
                    self.find_element(delete_button.format(i)).click()
                    time.sleep(1.5)
                for i in range(1, count+1):
                    print('输入各合同金额')
                    self.find_element(split_amount.format(i)).send_keys(contract_amount)
            elif 1 < len(self.find_elements(have_contact)) < count:
                d_value = count - len(self.find_elements(have_contact))
                print('进入第三个if,差值为:' + str(d_value))
                for i in range(1, len(self.find_elements(have_contact))+1):
                    print('输入各合同金额')
                    self.find_element(split_amount.format(i)).send_keys(contract_amount)
                for i in range(1, d_value+1):
                    print('拆分满个数')
                    self.find_element(plus_button.format(i)).click()
                    time.sleep(1.5)
            elif len(self.find_elements(have_contact)) == 1 and len(self.find_elements(have_contact)) < count:
                print('进入第四个if')
                self.find_element(split_amount.format('1')).send_keys(contract_amount)
                for i in range(1, count):
                    print('==========================')
                    self.find_element(plus_button.format(i)).click()
                    time.sleep(1.5)
            self.find_element(final_payment).click()
            self.find_element(submit).click()
            time.sleep(1)
            self.find_element(confirm).click()
            time.sleep(2)
            if channel == "线上":
                for i in range(1, count+1):
                    self.find_element(online_sign_button1.format(i)).click()
                    time.sleep(1)
                    self.find_element(sign_confirm).click()
                    time.sleep(1)
                    self.find_element(sign_confirm1).click()
                    time.sleep(1)
        else:
            if channel == "线上":
                self.find_element(online_sign_button).click()

    def hujin_assign(self, login_name_list):
        first_picture = '//img[@src="/aitoumobile/images/ht_04.c5a6239c.png"]'
        logout = '//a[@class="w_purebutton logout"]'
        login = '//input[1]'
        password = '//input[@placeholder="请输入密码"]'
        login_button = "//button[text()='登录']"
        wait_sign = '//div[@id="unSignListBox"]/div[@class="ht_module"]'
        go_sign = '//a[text()="前往签署"]'
        agree = '//a[text()="确认"]/following::input[1]'
        confirm = '//a[text()="确认"]'
        sure = '//a[text()="确定"]'

        # 打开线上签约页面签约
        new_window = 'window.open("https://testlffz.5aitou.com/aitoumobile/loanSearch/index")'
        self.driver.execute_script(new_window)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        # 判断是否为登录页
        if self.driver.current_url == 'https://testlffz.5aitou.com/aitoumobile/loanSearch/index':
            self.find_element(first_picture).click()
            time.sleep(2)
            self.find_element(logout).click()
            time.sleep(2)
        else:
            for i in range(len(login_name_list)):
                self.find_element(login).send_keys(login_name_list[i])
                self.find_element(password).send_keys('12345678w')
                self.find_element(login_button).click()
                time.sleep(2)
                self.find_element(first_picture).click()
                time.sleep(2)
                while len(self.find_elements(wait_sign)) > 0:
                    self.find_element(wait_sign).click()
                    time.sleep(2)
                    self.find_element(go_sign).click()
                    time.sleep(2)
                    self.find_element(agree).click()
                    time.sleep(2)
                    self.find_element(confirm).click()
                    time.sleep(2)
                    self.find_element(sure).click()
                    time.sleep(2)
                    self.driver.back()
                    self.driver.refresh()
                    time.sleep(1.5)
                self.find_element(logout).click()
                time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
