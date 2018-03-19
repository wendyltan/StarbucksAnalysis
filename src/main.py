#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


import os
from src.util import exceltosql as es
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
    #获得中国的店铺信息
    r3 = qr.get_country_store_info(table,'CN')

    count,position = qr.get_position(table,range='country',country_code='CN')
    print(count)
    print(position)

    #
    #
    # 绘制条形图
    # key1,value1 = hp.get_seperate_list(r1)
    # dc.gen_Bar(key1,value1,"Top 10 country and their stores")
    #
    # #绘制饼图
    # key2,value2 = hp.get_seperate_list(r2)
    # dc.gen_Pie(key2,value2,"4 ownership")
    #
    #根据数量绘制条形图
    # all_city_name = []
    # for item in r3[1]:
    #     all_city_name.append(item[0])
    #
    # key3= list(Counter(all_city_name).keys())
    # value3 = list(Counter(all_city_name).values())
    # dc.gen_Bar(key3,value3,"国内星巴克城市店面分布")
    #
    # country_city_topten = []
    # for item in r3[2]:
    #     country_city_topten.append(item)
    #
    # key4,value4 = hp.get_seperate_list(country_city_topten)
    #
    # dc.gen_Pie(key4,value4,"国内前十个店铺最多的城市")
    # #

