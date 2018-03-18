#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


import os
from src import exceltosql as es
from src import models as md
from src import query as qr
from src import drawChart as dc
from collections import Counter

def get_seperate_list(raw_result):
    key = []
    value = []

    for row in raw_result:
        key.append(row[0])
        value.append(row[1])
    return key,value

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



    # key1,value1 = get_seperate_list(r1)
    # dc.gen_Bar(key1,value1,"Top 10 country and their stores")
    #
    # key2,value2 = get_seperate_list(r2)
    # dc.gen_Pie(key2,value2,"4 ownership")


    all_city_name = []
    all_city_count = []
    for item in r3[1]:
        all_city_name.append(item[0])
    print(all_city_name)

    key = list(Counter(all_city_name).keys())
    print(key)
    value = list(Counter(all_city_name).values())
    dc.gen_Scatter(key,value)



