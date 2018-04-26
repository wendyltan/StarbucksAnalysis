#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


import sys
from src import query as qr
from src import table
import pandas as pd
from src.util import helper as hp
from src import drawChart as dc
from src import gui as br

if __name__ == '__main__':

    # #程序主循环
    # app = br.QApplication(sys.argv)
    # window = br.MainWindow()
    # window.show()
    # app.exec_()


    # 查询
    # 拥有星巴克的前十个国家
    # r1 = qr.get_number_of_country(table, 10)
    # 四个不同拥有权在全世界的比重
    # r2 = qr.get_ownership_percentage(table)
    # # 获得中国的店铺信息
    # r3 = qr.get_country_store_info(table, 'CN')
    # # 全世界的店铺范围和信息
    # position = qr.get_position(table, range='world')
    #


    # 根据数量绘制条形图
    # all_city_name = []
    # for item in r3[1]:
    #     all_city_name.append(item[0])
    #
    # key3= list(Counter(all_city_name).keys())
    # value3 = list(Counter(all_city_name).values())
    # dc.gen_Bar(key3,value3,"国内星巴克城市店面分布")

    # country_city_topten = hp.row_into_list(r3[2])
    #
    # key4,value4 = hp.get_seperate_list(country_city_topten)
    #
    # dc.gen_Pie(key4,value4,"国内前十个店铺最多的城市")

    starbucks = qr.get_dataFrame(table)
    # 测试数据：珠区经纬度
    aimlat = 22.25
    aimlng = 113.53
    k = 5

    # 第3次迭代，需求1
    # timezone = hp.timezone_statistics(starbucks)
    # starbucks = hp.set_timezone_color(starbucks,timezone)
    # dc.draw_map(starbucks,isTimeZone=True,isOpen=True)

    # 第3次迭代，需求2.1
    # 输入数据：aimlat:目标纬度，aimlng:目标经度,k:查找点数量
    # while True:
    #     aimlat,aimlng = map(float,input("纬度，经度：").split())
    #     if aimlat >= -90 and aimlat <= 90 and aimlng >= -180 and aimlng <= 180:
    #         break
    #     else:
    #         print("输入数据不合法！")
    #         continue
    #     k = int(input("K值："))
    #     if k > 0:
    #         break
    #     else:
    #         print("输入数据不合法！")
    #         continue
    # hp.top_k(aimlat, aimlng, starbucks, k,isShowInfo=True)

    # 第3次迭代，需求2.2
    # while True:
    #     aimlat,aimlng = map(float,input("纬度，经度：").split())
    #     if aimlat >= -90 and aimlat <= 90 and aimlng >= -180 and aimlng <= 180:
    #         break
    #     else:
    #         print("输入数据不合法！")
    #         continue
    # x_k = []
    # y_time = []
    # for k in range(1,31):
    #     t = hp.top_k(aimlat,aimlng,starbucks,k,isShowInfo=False,isReturnTime=True)
    #     x_k.append(k)
    #     y_time.append(t)
    # dc.gen_Bar(x_k,y_time,"随着K值得增长查询时延的变化",isOpen=True)


