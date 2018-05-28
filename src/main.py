#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


import sys
import pandas as pd
from src import drawChart as dc
from src import gui as br
from src import query as qr
from src.util import helper as hp
from src import table
import time
import os


if __name__ == '__main__':

    # 程序主循环
    app = br.QApplication(sys.argv)
    window = br.MainWindow()
    window.show()
    app.exec_()




    # 下面的代码和import的东西等迭代结束了再删掉，不然需要修改的话又得重新去找
    # starbucks = qr.get_dataFrame(table)
    # aimlat = 22.3
    # aimlng = 113.7
    # k = 5
    # r = 15

    # 读取评分记录
    # save_log = hp.grade_read(starbucks)
    # d_dict = hp.count_all_distance(aimlat, aimlng, starbucks)

    # top-k查询结果进行店铺评分
    # print("Top-K:")
    # k_list = hp.top_k(d_dict, k, isReturnList=True)
    # print(k_list)
    # match_topk = hp.change_to_matchdict(k_list, starbucks,save_log)

    # range查询结果进行店铺评分
    # print("Range:")
    # r_list = hp.top_r(d_dict, r, isReturnList=True)
    # match_range = hp.change_to_matchdict(r_list, starbucks,save_log)

    # 关键词查询结果进行店铺评分
    # print("Keyword-Select:")
    # keyword = "珠海"
    # keyword_list = hp.keyword_select(keyword, k, aimlat, aimlng, starbucks, isReturnList=True, isOpen=False)
    # match_keyword = hp.change_to_matchdict(keyword_list,starbucks,save_log)

    # 保存评分记录
    # hp.grade_save(save_log)





