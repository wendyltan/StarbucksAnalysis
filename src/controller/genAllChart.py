#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/7 20:19
# @Author  : Wendyltanpcy
# @File    : genAllChart.py
# @Software: PyCharm
import src.model.MyDF
import src.controller.no_frameobj_helper
from src.helper import query as qr, drawChart as dc
from src.model.MyDF import MyDataFrame
from src.controller import frameobj_helper as hp
from src import *
from src.view import observer
import time


class Gen():
    """
    Generate requirement charts in this class.Use gui to invoke the run method.
    """
    def __init__(self):
        # self.starbucks = qr.get_dataFrame(table)

        # starbucks is now a MyDataFrame object
        dataframe = qr.get_dataFrame(table)
        self.starbucks = MyDataFrame()
        self.starbucks.setDataFrame(dataframe)
        self.starbucks.setTable(table)

        # # 第2次迭代，需求1按经纬度绘制散点图
        dc.draw_map(self.starbucks.df, continent='world',folder='static/chartHtml/')
        #
        # # 第2次迭代，需求2按时区绘制地图
        self.starbucks = hp.set_random_color_for_df(self.starbucks, "Timezone")
        dc.draw_map(self.starbucks.df, continent='world', isTimeZone=True,folder='static/chartHtml/')
        #
        # # 第2次迭代，需求2按时区绘制条形图
        timezone = self.starbucks.count_number_to_dict("Timezone")
        x_timezone = []
        y_number = []
        # # 不排序
        for key, value in timezone.items():
            x_timezone.append(key)
            y_number.append(value)
        # # 排序，时区中数量多的排在前面
        for item in sorted(timezone.items(), key=lambda item: item[1], reverse=True):
            x_timezone.append(item[0])
            y_number.append(item[1])
        dc.gen_Bar(x_timezone, y_number, "2.2统计每个时区中星巴克的数量",folder='static/chartHtml/')
        #
        # # 第2次迭代，需求3按国家中星巴克数量绘制地图
        self.starbucks = self.starbucks.count_stabucks_quantity_for_df()
        self.starbucks = self.starbucks.change_alpha2_to_alpha3_for_df()
        dc.draw_map_by_country(self.starbucks.df, title="2.3全世界各国星巴克数量",folder='static/chartHtml/')
        #
        # # 第2次迭代，需求4按国家中星巴克数量绘制条形图
        country = {}
        x_country = []
        y_number = []
        for country_name in self.starbucks.df["Country"]:
            if country_name not in country:
                country[country_name] = 1
            if country_name in country:
                country[country_name] = country[country_name] + 1
        for item in sorted(country.items(), key=lambda item: item[1], reverse=True):
            x_country.append(item[0])
            y_number.append(item[1])
        dc.gen_Bar(x_country, y_number, "2.4统计每个国家拥有的星巴克数量",folder='static/chartHtml/')
        # # 画世界/亚洲等范围的地图

    def run(self, lon,lat, r_or_k,keyword=None,mode='k'):

        if(lon == 0 and lat == 0 and r_or_k == 0 and keyword == None and mode ==''):

            # # 第3次迭代，需求1
            self.starbucks.df.pop("Rgb Value")
            timezone = self.starbucks.count_number_to_dict("Timezone")
            self.starbucks = hp.set_timezone_color(self.starbucks,timezone)
            scl = [[0, "rgb(0,248,255)"],[0.01, "rgb(10,217,255)"],[0.02, "rgb(20,186,255)"],
                   [0.04, "rgb(31,155,255)"],[0.1, "rgb(41,124,255)"],[0.16, "rgb(51,93,225)"],
                   [0.3, "rgb(61,62,255)"],[0.6, "rgb(71,31,255)"],[1, "rgb(81,0,255)"]]
            dc.draw_map(self.starbucks.df,isTimeZone=True,isOpen=False,scl=scl,export=False,newtitle="3.1 店铺密度")

        # 第3次迭代，需求2.1。（用改进后的，后面再改改）

        aimlat = lat
        aimlng = lon
        if(mode=='k'):
            d_dict = hp.count_all_distance(aimlat,aimlng,self.starbucks)
            print(d_dict)
            # 第4次迭代，需求1改进，对于同一个k值，查询时延几乎不变。以下为查询k个点的需求。
            # 界面：替换掉第3次迭代中的需求2.1，但是记得保留原先代码中的用户输入部分
            # 用户输入：目标点经纬度，k值
            k_list = src.controller.no_frameobj_helper.top_k(d_dict, k=r_or_k, isReturnList=True)
            print(k_list)


            hp.show_info_in_map(aimlat, aimlng, self.starbucks,k_list, t='4.1')

            # 第3次迭代，需求2.2。（用改进后的，后面再改改）

            st = time.time()
            # 第4次迭代，需求1改进，以下为随着k增长，查询时延的折线图。
            # 界面：替换掉第3次迭代中的需求2.2，记得原先代码中的保留用户输入部分
            # 用户输入：目标点经纬度，k值
            src.controller.no_frameobj_helper.show_query_delay(d_dict, r_or_k, "K", st)
        elif(mode=='r'):



            # 第4次迭代，需求2.1，距离range查询
            # 用户输入：目标经纬度，距离半径r
            st = time.time()
            d_dict = hp.count_all_distance(aimlat, aimlng, self.starbucks)
            r_list = src.controller.no_frameobj_helper.top_r(d_dict, r=r_or_k, isReturnList=True)
            hp.show_info_in_map(aimlat, aimlng, self.starbucks, r_list, t='4.2.1')

            # 第4次迭代，需求2.2，展示range查询时延的变化
            # 用户输入：目标经纬度
            src.controller.no_frameobj_helper.show_query_delay(d_dict, r_or_k, "R", st)
        elif(mode=='m'):

            # 第4次迭代，需求3.1，k个完全匹配的店铺
            # 用户输入：搜索关键词keyword,目标经纬度，查找的数量k
            hp.keyword_select(keyword, r_or_k, aimlat, aimlng, self.starbucks)

        ob = observer.MapData()
        ob.set_measurement()
        print("All modeHtml generate success!")
        return True
