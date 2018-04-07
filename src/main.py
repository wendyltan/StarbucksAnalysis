#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


from collections import Counter
from tkinter import Tk
from pandas import DataFrame
from src import *
from src import query as qr
from src import drawChart as dc
from src import gui as g
from src.util import helper as hp
import pycountry

# 需要稍后重构的测试函数

def select(name):
    if name == '散点图':
        sandian()
    if name == '条形图':
        paint()


# # 绘制条形图
def paint():
    key1, value1 = hp.get_seperate_list(r1)
    dc.gen_Bar(key1, value1, "Top 10 country and their stores")


# #绘制饼图
def bing():
    key2, value2 = hp.get_seperate_list(r2)
    dc.gen_Pie(key2, value2, "4 ownership")


# 绘制不同时区的散点图
def sandian():
    starbucks = qr.get_dataFrame(table)  # 包含所有数据的数据集
    dc.draw_map(qr.get_dataFrame(table))




# 这个语句会使得tkinter不能调用绘制地图的方法
#  if __name__ == ('__main__' ):
# ---
# wendy:
# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
# 这句话的意思就是，当模块被直接运行时，以下代码块将被运行，
# 当模块是被导入时，代码块不被运行。
# ---

if __name__ == '__main__':
#
#     win = Tk()
#     win.title("星巴克数据分析")
#     app = g.App(win)
#     win.mainloop()

    # 查询
    # 拥有星巴克的前十个国家
    r1 = qr.get_number_of_country(table, 10)
    # 四个不同拥有权在全世界的比重
    r2 = qr.get_ownership_percentage(table)
    # # 获得中国的店铺信息
    r3 = qr.get_country_store_info(table, 'CN')
    # # 全世界的店铺范围和信息
    # position = qr.get_position(table, range='world')
    # #


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


    # 需求1按经纬度绘制散点图
    # starbucks = {}
    # result_list = hp.row_into_list(hp.get_seperate_list(position))
    # starbucks["Store Name"] = result_list[0]
    # starbucks["City"] = result_list[1]
    # starbucks["Longitude"] = result_list[2]
    # starbucks["Latitude"] = result_list[3]
    # starbucks = DataFrame(starbucks)
    # 画世界/亚洲等范围的地图
    # dc.draw_map(qr.get_dataFrame(table),continent='asia',export=False)

    # 需求2按时区绘制地图
    # starbucks = qr.get_dataFrame(table)
    # dc.draw_map(starbucks,continent='world')
    # dc.draw_map(starbucks,'world',isTimeZone=True)

    # 需求2按时区绘制条形图
    # starbucks = qr.get_dataFrame(table)
    # timezone = {}
    # x_timezone = []
    # y_number = []
    # for timezone_name in starbucks["Timezone"]:
    #     if timezone_name not in timezone:
    #         timezone[timezone_name] = 1
    #     if timezone_name in timezone:
    #         timezone[timezone_name] = timezone[timezone_name] + 1
    # # 不排序
    # for key,value in timezone.items():
    #     x_timezone.append(key)
    #     y_number.append(value)
    # 排序，时区中数量多的排在前面
    # for item in sorted(timezone.items(), key=lambda item: item[1], reverse=True):
    #     x_timezone.append(item[0])
    #     y_number.append(item[1])
    # dc.gen_Bar(x_timezone,y_number,"统计每个时区中星巴克的数量")

    # 需求3按国家中星巴克数量绘制地图
    # starbucks = qr.get_dataFrame(table)
    # starbucks = hp.count_stabucks_quantity_for_df(starbucks)
    # starbucks = hp.change_alpha2_to_alpha3_for_df(starbucks)
    # dc.draw_map_by_country(starbucks)

    # 需求4按国家中星巴克数量绘制条形图
    # starbucks = qr.get_dataFrame(table)
    # country = {}
    # x_country = []
    # y_number = []
    # for country_name in starbucks["Country"]:
    #     if country_name not in country:
    #         country[country_name] = 1
    #     if country_name in country:
    #         country[country_name] = country[country_name] + 1
    # for item in sorted(country.items(), key=lambda item: item[1], reverse=True):
    #     x_country.append(item[0])
    #     y_number.append(item[1])
    # dc.gen_Bar(x_country,y_number,"统计每个国家拥有的星巴克数量")

