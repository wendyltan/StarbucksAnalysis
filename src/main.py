#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


from collections import Counter
from pandas import DataFrame
from src import *
from src import query as qr
from src import drawChart as dc
from src.util import helper as hp

if __name__ == '__main__':


    #查询

    #拥有星巴克的前十个国家
    r1= qr.get_number_of_country(table,10)
    #四个不同拥有权在全世界的比重
    r2 = qr.get_ownership_percentage(table)
    #获得中国的店铺信息
    r3 = qr.get_country_store_info(table,'CN')
    #全世界的店铺范围和信息
    position = qr.get_position(table,range='world')
    #

    # # 绘制条形图
    # key1,value1 = hp.get_seperate_list(r1)
    # dc.gen_Bar(key1,value1,"Top 10 country and their stores")
    #
    # #绘制饼图
    # key2,value2 = hp.get_seperate_list(r2)
    # dc.gen_Pie(key2,value2,"4 ownership")
    #
    # # 根据数量绘制条形图
    # all_city_name = []
    # for item in r3[1]:
    #     all_city_name.append(item[0])
    #
    # key3= list(Counter(all_city_name).keys())
    # value3 = list(Counter(all_city_name).values())
    # dc.gen_Bar(key3,value3,"国内星巴克城市店面分布")
    #
    # country_city_topten = hp.row_into_list(r3[2])
    #
    # key4,value4 = hp.get_seperate_list(country_city_topten)
    #
    # dc.gen_Pie(key4,value4,"国内前十个店铺最多的城市")
    #

    # # 绘制地图
    # starbucks = {}
    # result_list = hp.row_into_list(hp.get_seperate_list(position))
    # starbucks["Store Name"] = result_list[0]
    # starbucks["City"] = result_list[1]
    # starbucks["Longitude"] = result_list[2]
    # starbucks["Latitude"] = result_list[3]
    # starbucks = DataFrame(starbucks)
    # #画世界/亚洲等范围的地图
    # dc.draw_map(qr.get_dataFrame(table),continent='asia',export=False)

    # 绘制不同时区的散点图
    # starbucks = {}
    # 需要迪哥的数据集!
    # starbucks["Store Name"] =
    # starbucks["Timezone"] =
    # starbucks["Longitude"] =
    # starbucks["Latitude"] =
    # dc.draw_map_by_timezone(qr.get_dataFrame(table))


