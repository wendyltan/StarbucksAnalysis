#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 20:19
# @Author  : Wendyltanpcy
# @File    : genAllChart.py
# @Software: PyCharm

from src import query as qr
from src import drawChart as dc
from src.util import helper as hp
from src import *

class Gen():
    """
    do not put this long smelly code in main. Use a class as a module import  instead
    """
    def run(self):
        # 需求1按经纬度绘制散点图
        starbucks = qr.get_dataFrame(table)
        # 画世界/亚洲等范围的地图
        dc.draw_map(qr.get_dataFrame(table), continent='asia', export=False)

        # 需求2按时区绘制地图
        dc.draw_map(starbucks, continent='world', isTimeZone=True)

        # 需求2按时区绘制条形图
        timezone = {}
        x_timezone = []
        y_number = []
        for timezone_name in starbucks["Timezone"]:
            if timezone_name not in timezone:
                timezone[timezone_name] = 1
            if timezone_name in timezone:
                timezone[timezone_name] = timezone[timezone_name] + 1
        # 不排序
        for key, value in timezone.items():
            x_timezone.append(key)
            y_number.append(value)
        # 排序，时区中数量多的排在前面
        for item in sorted(timezone.items(), key=lambda item: item[1], reverse=True):
            x_timezone.append(item[0])
            y_number.append(item[1])
        dc.gen_Bar(x_timezone, y_number, "统计每个时区中星巴克的数量")

        # 需求3按国家中星巴克数量绘制地图
        starbucks = hp.count_stabucks_quantity_for_df(starbucks)
        starbucks = hp.change_alpha2_to_alpha3_for_df(starbucks)
        dc.draw_map_by_country(starbucks, title="全世界各国星巴克数量")

        # 需求4按国家中星巴克数量绘制条形图
        country = {}
        x_country = []
        y_number = []
        for country_name in starbucks["Country"]:
            if country_name not in country:
                country[country_name] = 1
            if country_name in country:
                country[country_name] = country[country_name] + 1
        for item in sorted(country.items(), key=lambda item: item[1], reverse=True):
            x_country.append(item[0])
            y_number.append(item[1])
        dc.gen_Bar(x_country, y_number, "统计每个国家拥有的星巴克数量")

        print("All chartHtml generate success!")
        return True