#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm


from collections import Counter
from tkinter import Tk
import pycountry
import sys
from pandas import DataFrame
from src import gui as br
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit,QInputDialog
from src import gui

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=gui.MyWindow()
    myshow.show()
    sys.exit(app.exec_())
# if __name__ == '__main__':
#
#     #程序主循环
#     app = br.QApplication(sys.argv)
#     window = br.MainWindow()
#     window.show()
#     app.exec_()


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




