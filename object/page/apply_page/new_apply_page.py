from object.baseuse.base_func import *
from object.page.base_page.page_function import PageFunction
import time
import os


class NewApplyPage(BaseFunc):
    # (所有贷款类型)个人/企业公用字段
    bank = '//span[contains(text(),"银行名称")]/following::input[1]'
    bank_address = '//span[contains(text(),"开户行")]/following::input[1]'
    bank_card = '//span[contains(text(),"银行卡号")]/following::input[1]'
    email = '//span[contains(text(),"邮箱")]/following::input[1]'
    mobile = '//span[contains(text(),"联系电话")]/following::input[1]'
    industry = "//span[text()='所属行业']/following::input[1]"
    income = "//span[text()='收入情况']/following::input[1]"
    pic_exist = '//span[text()="附件"]//following::td//div//img'
    id_card_front = '//button[text()=" 上传身份证正面"]'
    id_card_back = '//button[text()=" 上传身份证反面"]'
    company_pic = '//button[text()=" 上传营业执照"]'
    # （所有贷款类型）企业公用字段
    registration_province = '//span[text()="注册省份"]/following::input[1]'
    registration_date0 = '//span[text()="企业年利润"]//preceding::i[@class="z-datebox-icon z-icon-calendar"][1]'
    registration_date1 = '//span[text()="企业名称"]//following::i[@class="z-datebox-icon z-icon-calendar"][1]'
    choose_date = '//iframe//following::td[1]'
    registered_capital = '//span[contains(text(),"企业年利润")]//preceding::span[contains(text(),"注册资金")][1]//' \
                         'following::input[1]'
    registered_capital1 = '//span[contains(text(),"企业年利润")]//following::span[contains(text(),"注册资金")][1]//' \
                          'following::input[1]'
    annual_return = '//span[contains(text(),"企业年利润")]/following::input[1]'
    main_business = '//span[contains(text(),"主营业务")]/following::textarea[1]'
    operating_period = '//span[contains(text(),"经营期限")]/following::textarea[1]'
    registered_address = '//span[contains(text(),"注册地址")]/following::textarea[1]'
    actual_business_address = '//span[contains(text(),"实际经营地址")]/following::textarea[1]'
    # （车贷）企业主借人独有字段
    registration_city = '//span[text()="注册城市"]/following::input[1]'
    ownership = '//span[text()="经营场所所有权"]/following::input[1]'
    # （车贷）个人主借人独有字段
    current_address = "//span[text()='现居地址']/following::input[1]"
    # (非车)个人/企业主借人公用字段
    educational = '//span[text()="学历"]/following::input[1]'
    educational1 = "//iframe/following::span[contains(text(),'本科')]"
    marital_status = '//span[text()="婚姻情况"]/following::input[1]'
    marital_status1 = '// iframe / following::span[contains(text(), "已婚")]'
    birth_place = '//span[text()="户口所在地"]/following::input[1]'
    address = '//span[text()="住宅地址"]/following::input[1]'
    residence_time = '//span[text()="起始居住时间"]/following::input[1]'
    residence_time1 = '//iframe/following::tr[2]/td[1]'
    native = '//span[text()="籍贯"]/following::input[1]'
    family_menber = '//span[text()="家庭成员"]/following::input[1]'
    occupation = '//span[text()="职业"]/following::input[1]'
    occupation1 = '//iframe/following::span[text()="律师"]'
    source_income = '//span[text()="收入来源"]/following::input[1]'
    source_income1 = '//iframe/following::span[text()="律师"]'
    # (非车)企业主借人独有字段
    plant_property_right = '//span[contains(text(),"厂房产权")]/following::input[1]'
    machine = '//span[contains(text(),"机器设备")]/following::input[1]'
    employees = '//span[contains(text(),"员工数量")]/following::input[1]'
    utilities = '//span[contains(text(),"水电费")]/following::input[1]'
    invoicing_situation = '//span[contains(text(),"开票情况")]/following::input[1]'

    def new_apply_page(self, loan_type, sub_type, amount, client_type, contact_no, contact_data_list):
        # 借款信息
        self.loan_info(loan_type, sub_type, amount)
        # 主借人信息
        self.customer_info(client_type, loan_type)
        # 过桥房屋信息
        if sub_type == '过桥':
            self.guoqiao_house()
        # 共签人
        if contact_no != 0:
            self.del_contact_user()
            for contact_data in contact_data_list:
                contact_name = contact_data.get('contact_name')
                contact_id = contact_data.get('contact_id')
                contact_type = contact_data.get('contact_type')
                self.add_contact_user(contact_no, loan_type, contact_name, contact_id, contact_type)
        else:
            self.del_contact_user()
        # 押品
        if sub_type == '房抵' or sub_type == '开心租':
            self.house()
        elif loan_type == '车贷信审':
            self.car()
        # # 上传附件
        # PageFunction(self.driver).upload_picture()

    def loan_info(self, loan_type, sub_type, amount):
        target = '//div[contains(text(),"借款信息")]'
        choose_product = '//span[contains(text(),"申请产品")]/following::input[1]'
        zy = '//iframe/following::div[contains(text()," 车辆质押-先息后本")]'
        zy1 = '//iframe/following::div[contains(text(),"3期")]'
        dy = '//iframe/following::div[contains(text()," 车辆抵押")]'
        dy1 = '//iframe/following::div[contains(text(),"车辆抵押-3")]'
        ry = '//iframe/following::div[contains(text(),"车商配资过户")]'
        ry1 = '//iframe/following::div[contains(text(),"3期")]'
        xy = '//iframe/following::div[contains(text()," 信用-先息后本")]'
        xy1 = '//iframe/following::div[contains(text(),"3期")]'
        gq = '//iframe/following::div[contains(text()," 过桥-先息后本")]'
        gq1 = '//iframe/following::div[contains(text(),"3期")]'
        fd = '//iframe/following::div[contains(text(),"CC")]'
        fd1 = '//iframe/following::div[contains(text(),"3期"])'
        f_loan_type = '//span[text()="团队经理"]/following::input[2]'
        happy_loan = '//div/ul/li/span[text()="开心租业务"]'
        house_loan = '//div/ul/li/span[text()="传统房抵业务"]'
        loan_use = '//label[text()="教育支出"]'
        apply_amount = '//span[text()="申请金额"]/following::input[1]'
        transfer_holder = '//button[contains(text(),"指定实际过户人")]'
        choose_holder = '//iframe/following::tbody[3]/tr[1]'

        self.wait_until_visible(target)
        self.find_element(apply_amount).send_keys(amount)
        self.find_element(loan_use).click()
        self.find_element(choose_product).click()
        if loan_type == '车贷信审':
            # 填写申请件信息-选择产品
            if sub_type == '车辆质押':
                time.sleep(2)
                self.find_element(zy).click()
                self.wait_until_visible(zy1)
                self.find_element(zy1).click()
            elif sub_type == '车辆抵押':
                time.sleep(2)
                self.find_element(dy).click()
                self.wait_until_visible(dy1)
                self.find_element(dy1).click()
            elif sub_type == '车辆让与担保':
                time.sleep(2)
                self.find_element(ry).click()
                self.wait_until_visible(ry1)
                self.find_element(ry1).click()
                time.sleep(1)
                self.find_element(transfer_holder).click()
                time.sleep(1.5)
                self.find_element(choose_holder).click()
        else:
            if loan_type == '房抵信审':
                # 填写申请件信息-选择产品
                time.sleep(2)
                self.find_element(fd).click()
                self.wait_until_visible(fd1)
                self.find_element(fd1).click()
                time.sleep(1)
                self.find_element(f_loan_type).click()
                if sub_type == '开心租':
                    self.find_element(happy_loan).click()
                else:
                    self.find_element(house_loan).click()
                time.sleep(1)
            else:
                # 填写申请件信息-选择产品
                if sub_type == '过桥':
                    time.sleep(2)
                    self.find_element(gq).click()
                    self.wait_until_visible(gq1)
                    self.find_element(gq1).click()
                    time.sleep(1)
                elif sub_type == '信用':
                    time.sleep(2)
                    self.find_element(xy).click()
                    self.wait_until_visible(xy1)
                    self.find_element(xy1).click()
                    time.sleep(1)

    def customer_info(self, client_type, loan_type):
        # (所有贷款类型)个人/企业公用字段
        self.find_element(self.bank).send_keys("111111")
        self.find_element(self.bank_address).send_keys("111111")
        self.find_element(self.bank_card).send_keys("111111")
        self.find_element(self.email).clear()
        self.find_element(self.email).send_keys("111111@qq.com")
        self.find_element(self.mobile).clear()
        self.find_element(self.mobile).send_keys("15800000000")
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.industry))
        self.find_element(self.industry).clear()
        self.find_element(self.industry).send_keys("金融业")
        time.sleep(1)
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.income))
        self.find_element(self.income).clear()
        self.find_element(self.income).send_keys("月收入10000元-50000元")

        if client_type == '企业':
            # （所有贷款类型）企业公用字段
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.registration_province))
            self.find_element(self.registration_province).clear()
            self.find_element(self.registration_province).send_keys("北京市")
            time.sleep(1)
            self.find_element(self.registration_date0).click()
            time.sleep(1)
            self.find_element(self.choose_date).click()
            time.sleep(1)
            self.find_element(self.registration_date1).click()
            time.sleep(1)
            self.find_element(self.choose_date).click()
            time.sleep(1)
            self.find_element(self.registered_capital).send_keys("111111")
            self.find_element(self.annual_return).send_keys("111111")
            self.find_element(self.main_business).send_keys("111111")
            self.find_element(self.operating_period).send_keys("111111")
            self.find_element(self.registered_address).send_keys("111111")
            self.find_element(self.actual_business_address).send_keys("111111")
            if len(self.find_elements(self.pic_exist)) == 1:
                self.find_element(self.id_card_back).click()
                time.sleep(2)
                os.system("C:\\Users\\tjl_b\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
                time.sleep(1.5)
        else:
            # （所有贷款类型）个人公用字段
            if len(self.find_elements(self.pic_exist)) == 1:
                self.find_element(self.id_card_front).click()
                time.sleep(2)
                os.system("C:\\Users\\tjl_b\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
                time.sleep(1.5)
                self.find_element(self.id_card_back).click()
                time.sleep(2)
                os.system("C:\\Users\\tjl_b\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
                time.sleep(1.5)
        if loan_type == '车贷信审':
            if client_type == '企业':
                # （车贷）企业主借人独有字段
                self.find_element(self.ownership).click()
                self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.registration_city))
                self.find_element(self.registration_city).clear()
                self.find_element(self.registration_city).send_keys("北京市")
                time.sleep(1)
            else:
                # （车贷）个人主借人独有字段
                self.find_element(self.current_address).send_keys('茅箭区二堰街办堰桥街5号1幢1-2-1')
        else:
            # (非车)个人/企业主借人公用字段
            self.find_element(self.educational).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.educational))
            self.find_element(self.educational).clear()
            self.find_element(self.educational1).click()
            time.sleep(1)
            self.find_element(self.marital_status).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.marital_status))
            self.find_element(self.marital_status).clear()
            self.find_element(self.marital_status1).click()
            time.sleep(1)
            self.find_element(self.birth_place).send_keys('陕西省西安市茅箭区二堰街办堰桥街5号1幢1-2-1')
            self.find_element(self.address).send_keys('陕西西安茅箭区二堰街办堰桥街5号1幢1-2-1')
            self.find_element(self.residence_time).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.residence_time))
            self.find_element(self.residence_time).clear()
            self.find_element(self.residence_time1).click()
            time.sleep(1)
            self.find_element(self.native).send_keys('1')

            self.find_element(self.family_menber).send_keys('1')
            self.find_element(self.occupation).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.occupation))
            self.find_element(self.occupation).clear()
            self.find_element(self.occupation1).click()
            time.sleep(1)
            self.find_element(self.source_income).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(self.source_income))
            self.find_element(self.source_income).clear()
            self.find_element(self.source_income1).click()

            # (非车)企业主借人独有字段
            if client_type == '企业':
                self.find_element(self.registered_capital1).send_keys('111')
                self.find_element(self.plant_property_right).send_keys("111111")
                self.find_element(self.machine).send_keys("111111")
                self.find_element(self.employees).send_keys("111111")
                self.find_element(self.utilities).send_keys("111111")
                self.find_element(self.invoicing_situation).send_keys("111111")

    def del_contact_user(self):
        contact_user = '//span[text()="共签人信息"]/following::div[2]//div/div[3]//tbody[1]//a'
        delete_button = '//i[@class="z-icon-trash-o"]'

        while len(self.find_elements(contact_user)) > 0:
            self.find_element(contact_user).click()
            self.wait_until_visible(delete_button)
            self.find_element(delete_button).click()
            time.sleep(1.5)

    def add_contact_user(self, contact_no, loan_type='', contact_name='', contact_id='', contact_type=''):
        delete_button = '//i[@class="z-icon-trash-o"]'
        add_button = '//span[text()="共签人信息"]/following::i[@class ="z-icon-plus"][1]'
        ct_type = '//span[text()="类型"]/following::label[text()="{}"]'
        ct_name = '//div[text()="共签人信息"]//following::span[text()="姓名"]//following::td[1]//input[1]'
        ct_id = '//div[text()="共签人信息"]//following::span[contains(text(),"身份证")]//following::td[1]//input[1]'
        id_card_front = '//div[text()="共签人信息"]//following::button[text()=" 上传身份证正面"]'
        id_card_back = '//div[text()="共签人信息"]//following::button[text()=" 上传身份证反面"]'
        company_pic = '//div[text()="共签人信息"]//following::button[text()=" 上传营业执照"]'
        # 个人/企业公用字段
        bank = '//div[text()="共签人信息"]//following::span[contains(text(),"银行名称")]/following::input[1]'
        bank_address = '//div[text()="共签人信息"]//following::span[contains(text(),"开户行")]/following::input[1]'
        bank_card = '//div[text()="共签人信息"]//following::span[contains(text(),"银行卡号")]/following::input[1]'
        email = '//div[text()="共签人信息"]//following::span[contains(text(),"邮箱")]/following::input[1]'
        mobile = '//div[text()="共签人信息"]//following::span[contains(text(),"联系电话")]/following::input[1]'
        industry = '//div[text()="共签人信息"]//following::span[text()="所属行业"]/following::input[1]'
        income = '//div[text()="共签人信息"]//following::span[text()="收入情况"]/following::input[1]'
        educational = '//div[text()="共签人信息"]//following::span[text()="学历"]/following::input[1]'
        educational1 = '//iframe/following::span[contains(text(),"本科")]'
        marital_status = '//div[text()="共签人信息"]//following::span[text()="婚姻情况"]/following::input[1]'
        marital_status1 = '//iframe/following::span[contains(text(),"已婚")]'
        birth_place = '//div[text()="共签人信息"]//following::span[text()="户口所在地"]/following::input[1]'
        address = '//div[text()="共签人信息"]//following::span[text()="住宅地址"]/following::input[1]'
        car_address = '//div[text()="共签人信息"]//following::span[text()="现居地址"]/following::input[1]'
        residence_time = '//div[text()="共签人信息"]//following::span[text()="起始居住时间"]/following::i[@class=' \
                         '"z-datebox-icon z-icon-calendar"]'
        residence_time1 = '//iframe//following::td[@class="z-calendar-cell z-calendar-weekend z-calendar-outside"][1]'
        native = '//div[text()="共签人信息"]//following::span[text()="籍贯"]/following::input[1]'
        family_menber = '//div[text()="共签人信息"]//following::span[text()="家庭成员"]/following::input[1]'
        relationship = '//div[text()="共签人信息"]//following::span[text()="与借款人关系"]/following::input[1]'
        # 企业字段
        company_name = '//div[text()="共签人信息"]//following::span[contains(text(),"企业名称")]/following::input[1]'
        company_id = '//div[text()="共签人信息"]//following::span[text()="社会统一信用编码"]/following::input[1]'
        company_id1 = '//div[text()="共签人信息"]//following::span[text()="社会统一信用代码"]/following::input[1]'
        registration_province = '//div[text()="共签人信息"]//following::span[text()="注册省份"]/following::input[1]'
        registration_city = '//div[text()="共签人信息"]//following::span[text()="注册城市"]/following::input[1]'
        ownership = '//span[text()="经营场所所有权"]/following::input[1]'
        registration_date = '//div[text()="共签人信息"]//following::span[contains(text(),"注册时间")]/following::input'
        registered_capital = '//div[text()="共签人信息"]//following::span[contains(text(),"注册资金")]/following::input[1]'
        annual_return = '//div[text()="共签人信息"]//following::span[contains(text(),"企业年利润")]/following::input[1]'
        main_business = '//div[text()="共签人信息"]//following::span[contains(text(),"主营业务")]/following::textarea[1]'
        operating_period = '//div[text()="共签人信息"]//following::span[contains(text(),"经营期限")]/following::textarea[1]'
        registered_address = '//div[text()="共签人信息"]//following::span[contains(text(),"注册地址")]/following::textarea[1]'
        actual_business_address = '//div[text()="共签人信息"]//following::span[contains(text(),"实际经营地址")]/following::textarea[1]'
        plant_property_right = '//div[text()="共签人信息"]//following::span[contains(text(),"厂房产权")]/following::input[1]'
        machine = '//div[text()="共签人信息"]//following::span[contains(text(),"机器设备")]/following::input[1]'
        employees = '//div[text()="共签人信息"]//following::span[contains(text(),"员工数量")]/following::input[1]'
        utilities = '//div[text()="共签人信息"]//following::span[contains(text(),"水电费")]/following::input[1]'
        invoicing_situation = '//div[text()="共签人信息"]//following::span[contains(text(),"开票情况")]/following::input[1]'
        save = '//button[contains(text(),"保存")]'

        self.find_element(add_button).click()
        self.wait_until_visible(delete_button)
        self.find_element(ct_type.format(contact_type)).click()
        self.find_element(ct_name).send_keys(contact_name)
        self.find_element(ct_id).send_keys(contact_id)
        # 个人/企业公用字段
        self.find_element(bank).send_keys("工商银行")
        self.find_element(bank).send_keys("工商银行")
        self.find_element(bank_address).send_keys("陕西省茅箭区二堰街办堰桥街5号1幢1-2-1")
        self.find_element(bank_card).send_keys("3655214588521145202")
        self.find_element(email).send_keys("111111@qq.com")
        self.find_element(mobile).send_keys("15800000000")
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(industry))
        self.find_element(industry).send_keys("金融业")
        time.sleep(1)
        self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(income))
        self.find_element(income).send_keys("月收入10000元-50000元")
        if contact_type == '个人' or loan_type != '车贷信审':
            # 个人字段
            self.find_element(educational).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(educational))
            self.find_element(educational).clear()
            self.find_element(educational1).click()
            time.sleep(1)
            self.find_element(marital_status).click()
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(marital_status))
            self.find_element(marital_status).clear()
            self.find_element(marital_status1).click()
            time.sleep(1)
            self.find_element(birth_place).send_keys('陕西茅箭二堰街办堰桥街5号1幢1-2-1')
            if loan_type != '车贷信审':
                self.find_element(address).send_keys('陕省箭区二堰街办堰桥街5号1幢1-2-1')
            else:
                self.find_element(car_address).send_keys('1111111111')
            self.find_element(residence_time).click()
            self.find_element(residence_time1).click()
            time.sleep(1)
            self.find_element(native).send_keys('1')
            self.find_element(family_menber).send_keys('1')
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(relationship))
            self.find_element(relationship).send_keys('夫妻')
        if contact_type == '企业':
            # 企业字段
            self.find_element(company_name).send_keys("1")
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(registration_province))
            self.find_element(registration_province).send_keys("北京市")
            self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(registration_date))
            self.find_element(registration_date).send_keys('2000-01-01')
            self.find_element(registered_capital).send_keys("111111")
            self.find_element(annual_return).send_keys("111111")
            self.find_element(main_business).send_keys("111111")
            self.find_element(operating_period).send_keys("111111")
            self.find_element(registered_address).send_keys("111111")
            self.find_element(actual_business_address).send_keys("111111")
            if len(self.find_elements(company_pic)) == 1:
                self.find_element(id_card_back).click()
                time.sleep(2)
                os.system("C:\\Users\\tjl_b\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
                time.sleep(1.5)
            if loan_type != '车贷信审':
                self.find_element(company_id).send_keys("1")
                self.find_element(plant_property_right).send_keys("111111")
                self.find_element(machine).send_keys("111111")
                self.find_element(employees).send_keys("111111")
                self.find_element(utilities).send_keys("111111")
                self.find_element(invoicing_situation).send_keys("111111")
            else:
                self.find_element(company_id1).send_keys("1")
                self.driver.execute_script('arguments[0].removeAttribute("readonly")', self.find_element(registration_city))
                self.find_element(registration_city).send_keys("北京市")
                self.find_element(ownership).click()
        else:
            # （所有贷款类型）个人公用字段
            if len(self.find_elements(self.pic_exist)) == 0:
                self.find_element(id_card_front).click()
                time.sleep(2)
                os.system("C:\\Users\\tjl_b\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
                time.sleep(1.5)
                self.find_element(id_card_back).click()
                time.sleep(2)
                os.system("C:\\Users\\tjl_b\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
                time.sleep(1.5)
        self.find_element(save).click()

    def guoqiao_house(self):
        name = '//div[contains(text(),"买房人信息")]/following::input[1]'
        id_no = '//div[contains(text(),"买房人信息")]/following::input[2]'
        mobile = '//span[contains(text(),"身份证号")]/following::input[2]'
        address = '//span[contains(text(),"身份证号")]/following::input[4]'
        birth_place = '//span[contains(text(),"身份证号")]/following::input[5]'
        married = '//span[contains(text(),"身份证号")]/following::input[3]'
        married1 = '//iframe/following::span[contains(text(),"已婚")]'
        house_loantype = '//span[contains(text(),"抵押类型")]/following::input[1]'
        loans = '//span[contains(text(),"贷款余额")]/following::input[1]'
        floar_age = '//span[contains(text(),"贷款余额")]/following::input[2]'
        sales_price = '//span[contains(text(),"出售价格")]/following::input[1]'
        front_money = '//span[contains(text(),"出售定金")]/following::input[1]'
        down_payment = '//span[contains(text(),"出售首付款")]/following::input[1]'
        trustee_amount = '//span[contains(text(),"托管金额")]/following::input[1]'
        balance_payment = '//span[contains(text(),"交易尾款")]/following::input[1]'
        property_address = '//span[contains(text(),"交易尾款")]/following::input[2]'
        house_picture = '//button[text()=" 上传房产证照片"]'

        # 买房人信息
        self.find_element(name).send_keys("111111")
        self.find_element(id_no).send_keys("110101199307150088")
        self.find_element(mobile).send_keys("15800000000")
        self.find_element(address).send_keys("111111")
        self.find_element(birth_place).send_keys("111111")
        self.find_element(married).click()
        self.wait_until_visible(married1)
        self.find_element(married1).click()
        time.sleep(1)
        # 房产信息
        self.find_element(house_loantype).click()
        self.find_element(loans).send_keys("111111")
        self.find_element(floar_age).send_keys("111111")
        self.find_element(sales_price).send_keys("111111")
        self.find_element(front_money).send_keys("111111")
        self.find_element(down_payment).send_keys("111111")
        self.find_element(trustee_amount).send_keys("111111")
        self.find_element(balance_payment).send_keys("111111")
        self.find_element(property_address).send_keys("上海市杨浦区武东路198号")
        if len(self.find_elements(house_picture)) != 0:
            self.find_element(house_picture).click()
            time.sleep(2)
            os.system("C:\\Users\\Administrator\\PycharmProjects\\Test_framework\\data\\up_pic.exe")
            time.sleep(1.5)

    def house(self):
        plus_button = '//span[text()="关联押品"]//following::i[@class="z-icon-plus"][1]'
        tag = '//div[text()="新增押品 "]'
        choose_guarantee = '//span[contains(text(),"关联评估工单")]/following::input[1]'
        guarantee = '//div[contains(text(),"评估总价")]/following::tbody[2]/tr[1]/td[1]'
        confirm = '//button[contains(text(),"确认关联")]'
        time_from = '//span[contains(text(),"居住年限")]/following::input[1]'
        time_from1 = '//div/following::tbody/following::tr/following::td[text()="一月"]'
        time_to = '//span[contains(text(),"居住年限")]/following::input[2]'
        time_to2 = '//div/following::tbody/following::tr/following::td[text()="十二月"]'
        owner = '//span[contains(text(),"抵押人")]/following::input[1]'
        court = '//span[contains(text(),"管辖法院")]/following::input[1]'
        court1 = '//iframe/following::div/following::span[text()="抵押物所在地人民法院"]'
        save = '//button[contains(text(),"保存")]'
        save1 = '//button[contains(text(),"是")]'

        self.find_element(plus_button).click()
        self.wait_until_visible(tag)
        self.find_element(choose_guarantee).click()
        self.find_element(guarantee).click()
        self.find_element(confirm).click()
        self.find_element(time_from).click()
        self.wait_until_visible(time_from1)
        self.find_element(time_from1).click()
        time.sleep(1)
        self.find_element(time_to).click()
        self.wait_until_visible(time_to2)
        self.find_element(time_to2).click()
        time.sleep(1)
        self.find_element(owner).click()
        self.find_element(court).click()
        self.wait_until_visible(court1)
        self.find_element(court1).click()
        time.sleep(1)
        self.find_element(save).click()
        time.sleep(1)
        self.find_element(save1).click()
        time.sleep(1)

    def car(self):
        # 添加车抵押品
        plus_button = '//span[text()="关联押品"]//following::i[@class="z-icon-plus"][1]'
        tag = '//div[text()="新增押品 "]'
        frame_number = '//span[text()="车架号"]/following::input[1]'
        name = '//span[contains(text(),"车主姓名")]/following::input[1]'
        id = '//span[contains(text(),"车主证件号")]/following::input[1]'
        court = '//span[contains(text(),"管辖法院名称")]/following::input[1]'
        garage = '//span[contains(text(),"所属车库")]/following::input[1]'
        registration_certificate_no = '//span[contains(text(),"登记证书编号")]/following::input[1]'
        owner = '//span[contains(text(),"抵押人")]/following::input[1]'
        get_report = '//button[contains(text(),"获取好车伯乐报告")]'
        save = '//button[contains(text(),"保存")]'

        self.find_element(plus_button).click()
        self.wait_until_visible(tag)
        self.find_element(frame_number).send_keys('WP1AB2957FLB56258')
        self.find_element(name).send_keys('邓忠')
        self.find_element(id).send_keys('110101200001040041')
        self.find_element(court).send_keys('11111')
        self.find_element(garage).send_keys('11111')
        self.find_element(registration_certificate_no).send_keys('11111')
        self.find_element(owner).click()
        self.find_element(get_report).click()
        result = EC.alert_is_present()(self.driver)  # from selenium.webdriver.support import expected_conditions as EC
        if result:
            result.accept()
            brand = '//span[contains(text(),"车辆品牌")]/following::input[1]'
            car_model = '//span[contains(text(),"车辆型号")]/following::input[1]'
            plate_number = '//span[contains(text(),"车牌号(旧)")]/following::input[1]'
            car_type = '//span[contains(text(),"车辆类型")]/following::input[1]'
            value = '//span[contains(text(),"市场价值")]/following::input[1]'
            used_years = '//span[contains(text(),"已使用年")]/following::input[1]'
            color = '//span[contains(text(),"车辆颜色")]/following::input[1]'
            engine_number = '//span[contains(text(),"发动机号")]/following::input[1]'
            mileage = '//span[contains(text(),"行驶里程")]/following::input[1]'
            transfer_times = '//span[contains(text(),"过户次数")]/following::input[1]'
            production_date = '//span[contains(text(),"出厂日期")]/following::input[1]'
            production_date1 = '//iframe/following::table[@class="z-calendar-body"]//tr[1]/td[text()="1"]'
            seat = '//span[contains(text(),"座位数")]/following::input[1]'
            operation_situation = '//span[contains(text(),"运营情况")]/following::input[1]'
            registration_date = '//span[contains(text(),"初次登记日期")]/following::input[1]'
            registration_date1 = '//iframe/following::table[@class="z-calendar-body"][2]//tr[1]/td[text()="1"]'
            self.find_element(brand).send_keys('11111')
            self.find_element(car_model).send_keys('11111')
            self.find_element(plate_number).send_keys('沪C11111')
            self.find_element(car_type).send_keys('11111')
            self.find_element(value).send_keys('111')
            self.find_element(used_years).send_keys('1')
            self.find_element(color).send_keys('11111')
            self.find_element(engine_number).send_keys('11111')
            self.find_element(mileage).send_keys('11111')
            self.find_element(transfer_times).send_keys('11111')
            self.find_element(production_date).click()
            self.wait_until_visible(production_date1)
            self.find_element(production_date1).click()
            time.sleep(1)
            self.find_element(seat).send_keys('11111')
            self.find_element(operation_situation).send_keys('11111')
            self.find_element(registration_date).click()
            self.wait_until_visible(registration_date1)
            self.find_element(registration_date1).click()
            time.sleep(1)
            # 上传车辆照片附件
        self.find_element(save).click()

