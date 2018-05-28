#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 10:27
# @Author  : Wendyltanpcy
# @File    : scoreTable.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from src.util import helper as hp

class MyTable(QTableWidget):
    def __init__(self,match_topk,saveLog):
        super(QTableWidget, self).__init__()
        self.setWindowTitle("My Table")
        self.resize(600, 300)
        self.setRowCount(4)
        self.setColumnCount(4)
        self.match =match_topk
        self.savelog = saveLog

        # hp.score(self.match,self.savelog)
        # 设置表头
        self.setHorizontalHeaderLabels(['编号', '店铺名', '评分','标记'])
        self.setVerticalHeaderLabels(['第一行', '第二行', '第三行','第四行'])
        # 设置为只读状态
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置为选中一行，默认为选中单格
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 隐藏列表头
        # tableWidget.verticalHeader().setVisible(False);
        # 隐藏行表头
        # tableWidget.horizontalHeader().setVisible(False);

        # for i in range(5):
        #     for j in range(5):
        #         self.setItem(i, j, QTableWidgetItem(str(i) + str(j)))
        self.show()
    def closeEvent(self, *args, **kwargs):
        hp.grade_save(self.savelog)
        self.close()

