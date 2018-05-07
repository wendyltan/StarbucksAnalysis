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

    # 需求4.1改进，对于同一个k值，查询时延几乎不变。
    starbucks = qr.get_dataFrame(table)
    aimlat = 22.3
    aimlng = 113.7
    c = 1
    st = time.time()
    d_dict = hp.count_all_distance(aimlat,aimlng,starbucks)
    # 以下为查询k个点的需求。
    # hp.top_k(aimlat,aimlng,starbucks,d_dict,k=c,isShowInfo=True,isOpenHtml=False)

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
