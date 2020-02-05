#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time

# 项目路径
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

prj_path = os.path.dirname(os.path.dirname(__file__))  # 当前文件的上一级目录
data_path = os.path.join(prj_path, 'data')  # 数据目录
report_file = os.path.join(prj_path, 'report', 'report_{}.html'.format(now))  # 更改路径到report目录下


# 数据库配置
db_host = 'sh-cdb-0auhvizu.sql.tencentcdb.com'
db_port = 62736
db_user = 'root'
db_password = 'db!N70ES65#ac'
db = 'loan_test'

# DY("房抵", "DY", "z-icon-building", false, false),
# TRADITION_HOUSE("传统房抵业务", "TRADITION_HOUSE", LOAN_TYPE.DY), RENT_HOUSE("开心租业务", "RENT_HOUSE", LOAN_TYPE.DY);
# ZY("车辆质押", "ZY","z-icon-car", true, true),
# CD("车辆抵押Bak", "CD", "z-icon-car", true, null),
# BZ("保证", null, "", true, null),
# CSZY("车辆配资质押", "CSZY", "z-icon-car", true, null),
# GH("车辆让与担保", "GH", "z-icon-car", true, true),
# CSDY("车辆抵押","CSDY", "z-icon-car", true, true),
# CREDIT("信用", "CREDIT", "z-icon-credit-card", false, false),
# CCG("应收账款质押", "CCG", "z-icon-rmb", true, false),
# GQD("过桥", "GQD", "z-icon-building", false, false);
loan_type = {'DY': '房抵信审', 'CREDIT': '过桥信审', 'GQD': '过桥信审', 'ZY': '车贷信审', 'GH': '车贷信审', 'CSDY': '车贷信审'}
sub_type = {'TRADITION_HOUSE': '房抵', 'RENT_HOUSE': '开心租', 'CREDIT': '信用', 'GQD': '过桥', 'ZY': '车辆质押', 'GH': '车辆让与担保', 'CSDY': '车辆抵押'}
