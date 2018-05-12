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

if __name__ == '__main__':

    # 程序主循环
    # app = br.QApplication(sys.argv)
    # window = br.MainWindow()
    # window.show()
    # app.exec_()

    # 测试数据
    starbucks = qr.get_dataFrame(table)
    aimlat = 22.27
    aimlng = 114
    c = 480
    st = time.time()
    d_dict = hp.count_all_distance(aimlat,aimlng,starbucks)

    # 第4次迭代，需求1改进，对于同一个k值，查询时延几乎不变。以下为查询k个点的需求。
    # k_list = hp.top_k(d_dict,k=c,isReturnList=True,isReturnTime=False)
    # hp.show_info_in_map(aimlat,aimlng,starbucks,k_list,t='4.1',isOpenHtml=True)

    # 第4次迭代，需求1改进，以下为随着k增长，查询时延的折线图。
    # hp.show_query_delay(d_dict,c,"K",st,isOpenHtml=True)

    # 第4次迭代，需求2.1，距离range查询
    # c = 50
    # r_list = hp.top_r(d_dict,r=c, isReturnList=True,isReturnTime=False)
    # hp.show_info_in_map(aimlat,aimlng,starbucks,r_list,t='4.2',isOpenHtml=False)

    # 第4次迭代，需求2.2，展示range查询时延的变化
    # hp.show_query_delay(d_dict,c,"R",st,isOpenHtml=True)
