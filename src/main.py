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
    c = 100
    st = time.time()
    d_dict = hp.count_all_distance(aimlat,aimlng,starbucks)

    # 第4次迭代，需求1改进，对于同一个k值，查询时延几乎不变。以下为查询k个点的需求。
    # k_list = hp.top_k(d_dict,k=c,isReturnList=True,isReturnTime=False)
    # hp.show_info_in_map(aimlat,aimlng,starbucks,k_list,t='4.1',isOpenHtml=True)

    # 需求4.1改进，以下为随着k增长，查询时延的折线图。
    # x_k = []
    # y_time = []
    # if  c <= 500:
    #     for k in range(1, c + 1):
    #         t = hp.top_k(aimlat, aimlng, starbucks, d_dict, k, isShowInfo=False, isReturnTime=True)
    #         x_k.append(k)
    #         y_time.append(t)
    #     et = time.time()
    #     runtime = et - st
    #     print("总运行时间为：%.3f%s" %(runtime,'s'))
    # else:
    #     for k in range(1,c+1,35):
    #         t = hp.top_k(aimlat, aimlng, starbucks, d_dict, k, isShowInfo=False, isReturnTime=True)
    #         x_k.append(k)
    #         y_time.append(t)
    #     et = time.time()
    #     runtime = et - st
    #     print("总运行时间为：%.3f%s" %(runtime,'s'))
    # dc.draw_line_plot(x_k, y_time, "随着K值得增长查询时延的变化", isOpen=True)
    # dc.gen_Scatter(y_time,x_k,"随着K值得增长查询时延的变化",isOpen=True)

    # 第4次迭代，需求2，距离range查询
    # c = 50
    # r_list = hp.top_r(d_dict,r=c, isReturnList=True,isReturnTime=False)
    # hp.show_info_in_map(aimlat,aimlng,starbucks,r_list,t='4.2',isOpenHtml=False)
