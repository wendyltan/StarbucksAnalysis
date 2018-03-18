#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm

import numpy as np
import os
from src import exceltosql as es
from src import models as md
from src import query as qr

if __name__ == '__main__':
    file_name = 'dataset/dataset.xlsx'
    db_name = 'starbucks.db'
    if not os.path.exists(db_name):
        # transfer excel to database
        es.doTransfer(file_name,db_name)
    table = md.Starbuck

    #查询

    #拥有星巴克的前十个国家
    r1= qr.get_number_of_country(table,10)
    #四个不同拥有权在全世界的比重
    r2 = qr.get_ownership_percentage(table)
    #指定的城市的星巴克分布概况，包括总店铺数和店铺概况列表
    r3 = qr.get_country_store_info(table,'CN')

    print(r1,'\n',r2,'\n',r3)






