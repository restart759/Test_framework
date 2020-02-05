import pymysql
from config.config import *


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host=db_host,
                                    port=db_port,
                                    user=db_user,
                                    passwd=db_password,
                                    db=db)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def check_login_name(self, apply_no):
        apply_no_list = []
        sql1 = '''SELECT c.login FROM wealth_web_user c 
                        WHERE c.identity = (
                        SELECT b.id_no FROM aitou_credit_apply_customer_info b 
                        INNER JOIN aitou_credit_apply a on a.id=b.fk_apply 
                        WHERE a.apply_no = "{}")'''
        sql2 = '''SELECT c.login FROM wealth_web_user c 
                        WHERE c.identity in (
                        SELECT b.id_no FROM aitou_credit_apply_contact_info b 
                        INNER JOIN aitou_credit_apply a on a.id=b.fk_apply 
                        WHERE a.apply_no = "{}")'''
        result1 = self.query(sql1.format(apply_no))
        apply_no_list.append(result1[0][0])
        result2 = self.query(sql2.format(apply_no))
        for i in range(len(result2)):
            apply_no_list.append(result2[i][0])
        return apply_no_list

    def check_apply_status(self, apply_no):
        sql = 'SELECT a.detail_business_type, a.loan_type, a.`status` FROM aitou_credit_apply a WHERE apply_no = "{}"'
        result = self.query(sql.format(apply_no))
        return result[0]

    def search_outing_pic_key(self, apply_no):
        sql = '''SELECT b.id FROM aitou_credit_apply_guarantee b 
                        INNER JOIN aitou_credit_apply a on a.id = b.fk_apply 
                        WHERE apply_no = '{}' 
                        LIMIT 1'''
        result = self.query(sql.format(apply_no))
        return result[0][0]

    def insert_outing_pic(self, table_id_list, table_key):
        sql = '''INSERT INTO aitou_attachment VALUES
                ('{0}',now(),'anonymousUser','1',NOW(),'anonymousUser',0,'1569747015684.jpg',
                'jpg','net.zkbc.aitou.entity.CreditApplyGuarantee','imageListOutVisitTransient','{1}',
                'CreditApplyGuarantee/{2}/imageListOutVisitTransient','credit-test','OUT_VISITING_PROVE_PIC',
                'ORIGINAL_PIC'),
                ('{3}',now(),'anonymousUser','1',NOW(),'anonymousUser',0,'1569747015684.jpg',
                'jpg','net.zkbc.aitou.entity.CreditApplyGuarantee','imageListOutFamilyLocationTransient','{4}',
                'CreditApplyGuarantee/{5}/imageListOutFamilyLocationTransient','credit-test','OUT_VISITING_HOUSE_LOCATION_PIC',
                'ORIGINAL_PIC'),
                ('{6}',now(),'anonymousUser','1',NOW(),'anonymousUser',0,'1569747015684.jpg',
                'jpg','net.zkbc.aitou.entity.CreditApplyGuarantee','imageListOutFamilyStateTransient','{7}',
                'CreditApplyGuarantee/{8}/imageListOutFamilyStateTransient','credit-test','OUT_VISITING_HOUSE_STATE_PIC',
                'ORIGINAL_PIC')'''
        self.exec(sql.format(table_id_list[0], table_key, table_key, table_id_list[1], table_key, table_key,
                             table_id_list[2], table_key, table_key))

    def update_basic_credit(self, apply_no):
        customer_sql = '''UPDATE aitou_credit_apply_customer_info
                          SET central_bank_overdue_amt = '1', central_bank_no_overdue_amt = '1', credit_card_overdue = '1', credit_card_no_overdue = '1', szx_overdue = '1',
                            szx_no_overdue = '1', guarantee_overdue = '1', guarantee_no_overdue = '1', month_valid_flow = '1', interest_march = '1', interest_june = '1', interest_september = '1',
                            interest_december = '1', input1amt = '1', input2amt = '1', input3amt = '1', input4amt = '1', input5amt = '1', input6amt = '1', output1amt = '1', output2amt = '1',
                            output3amt = '1', output4amt = '1', output5amt = '1', output6amt = '1', central_bank_overdue_cnt = '1', central_bank_overdue_total_amt = '1', central_bank_overdue_balance = '1',
                            central_bank_no_overdue_cnt = '1', central_bank_no_overdue_total_amt = '1', central_bank_no_overdue_balance = '1', credit_card_overdue_cnt = '1', credit_card_overdue_total_amt = '1',
                            credit_card_overdue_balance = '1', credit_card_no_overdue_cnt = '1', credit_card_no_overdue_total_amt = '1', credit_card_no_overdue_balance = '1', month_total_pay_amt = '1',
                            guarantee_overdue_balance = '1', guarantee_no_overdue_balance = '1'
                          WHERE fk_apply IN (SELECT id FROM aitou_credit_apply WHERE apply_no='{}')'''
        self.exec(customer_sql.format(apply_no))

        contact_sql = '''UPDATE aitou_credit_apply_contact_info
                         SET central_bank_overdue_amt = '1', central_bank_no_overdue_amt = '1', credit_card_overdue = '1', credit_card_no_overdue = '1', szx_overdue = '1',
                            szx_no_overdue = '1', guarantee_overdue = '1', guarantee_no_overdue = '1', month_valid_flow = '1', interest_march = '1', interest_june = '1', interest_september = '1',
                            interest_december = '1', input1amt = '1', input2amt = '1', input3amt = '1', input4amt = '1', input5amt = '1', input6amt = '1', output1amt = '1', output2amt = '1',
                            output3amt = '1', output4amt = '1', output5amt = '1', output6amt = '1', central_bank_overdue_cnt = '1', central_bank_overdue_total_amt = '1', central_bank_overdue_balance = '1',
                            central_bank_no_overdue_cnt = '1', central_bank_no_overdue_total_amt = '1', central_bank_no_overdue_balance = '1', credit_card_overdue_cnt = '1', credit_card_overdue_total_amt = '1',
                            credit_card_overdue_balance = '1', credit_card_no_overdue_cnt = '1', credit_card_no_overdue_total_amt = '1', credit_card_no_overdue_balance = '1', month_total_pay_amt = '1',
                            guarantee_overdue_balance = '1', guarantee_no_overdue_balance = '1'
                         WHERE fk_apply IN (SELECT id FROM aitou_credit_apply WHERE apply_no='{}')'''
        self.exec(contact_sql.format(apply_no))
