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
import time
import Levenshtein as le
from fuzzywuzzy import fuzz

if __name__ == '__main__':

    # 程序主循环
    app = br.QApplication(sys.argv)
    window = br.MainWindow()
    window.show()
    app.exec_()

    # 直接运行可以看到这次迭代的所有结果
    # 由于不是很清楚界面那边，需要用户输入的数据都写在下面的注释里了，还有啥问题随时沟通
    # 测试数据
    starbucks = qr.get_dataFrame(table)
    aimlat = 22.27
    aimlng = 114
    c = 480
    st = time.time()
    d_dict = hp.count_all_distance(aimlat,aimlng,starbucks)

    # 第4次迭代，需求1改进，对于同一个k值，查询时延几乎不变。以下为查询k个点的需求。
    # 界面：替换掉第3次迭代中的需求2.1，但是记得保留原先代码中的用户输入部分
    # 用户输入：目标点经纬度，k值
    k_list = hp.top_k(d_dict,k=c,isReturnList=True,isReturnTime=False)
    hp.show_info_in_map(aimlat,aimlng,starbucks,k_list,t='4.1',isOpenHtml=True)

    # 第4次迭代，需求1改进，以下为随着k增长，查询时延的折线图。
    # 界面：替换掉第3次迭代中的需求2.2，记得原先代码中的保留用户输入部分
    # 用户输入：目标点经纬度，k值
    hp.show_query_delay(d_dict,c,"K",st,isOpenHtml=True)

    # 第4次迭代，需求2.1，距离range查询
    # 用户输入：目标经纬度，距离半径r
    c = 50
    r_list = hp.top_r(d_dict,r=c, isReturnList=True,isReturnTime=False)
    hp.show_info_in_map(aimlat,aimlng,starbucks,r_list,t='4.2.1',isOpenHtml=True)

    # 第4次迭代，需求2.2，展示range查询时延的变化
    # 用户输入：目标经纬度
    hp.show_query_delay(d_dict,c,"R",st,isOpenHtml=True)

    # 第4次迭代，需求3.1，k个完全匹配的店铺
    # 用户输入：搜索关键词keyword,目标经纬度，查找的数量k
    keyword1 = "珠海"
    k1 = 20
    hp.keyword_select(keyword1,k1,aimlat,aimlng,starbucks,isOpen=True)
    keyword2 = "珠海市"
    k2 = 5
    hp.keyword_select(keyword2,k2,aimlat,aimlng,starbucks,isOpen=True)
