#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 10:27
# @Author  : Wendyltanpcy
# @File    : scoreTable.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from src.util import helper as hp

class MyTable(QWidget):
    def __init__(self,title,match,log):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(600, 300)
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.match =match
        self.messageBox = QMessageBox(self)

        self.log = log
        self.counter = 0
        self.btn_save = QPushButton('保存')
        self.btn_save.clicked.connect(self.save)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn_save)
        self.vbox.addWidget(self.table)

        label_list = []
        for key in self.match.items():
            self.counter += 1
            label_list.append(str(self.counter))

        self.table.setRowCount(self.counter)

        # 设置表头
        self.table.setHorizontalHeaderLabels(['编号', '店铺名', '评分'])
        self.table.setVerticalHeaderLabels(label_list)

        self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.table.editable = True
        # 设置为选中一行，默认为选中单格
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)


        for key,values in self.match.items():
            self.table.setItem(key-1,0,QTableWidgetItem(values['index']))
            self.table.setItem(key-1,1,QTableWidgetItem(values['Store Name']))
            if ( values['Grade']!=''and float(values['Grade']) >=8):
                print("match")
                gradeItem = QTableWidgetItem(str(values['Grade']))
                # can not set the cell color?
                # gradeItem.setBackground(U)
                self.table.setItem(key - 1, 2, gradeItem)
            else :
                print("no match")
                self.table.setItem(key - 1, 2, QTableWidgetItem(str(values['Grade'])))

        self.setLayout(self.vbox)
        self.table.cellChanged.connect(self.contentChange)
        if (len(self.match) == 0):
            self.messageBox.warning(self, "Warning", "r or k too small to find any datas!",QMessageBox.Ok)
            self.destroy()
        else:
            self.show()

    def save(self):
        # may have to write it back to the log
        hp.grade_save(save_log=self.log)

    def contentChange(self,row,col):
        item = self.table.item(row, col)
        txt = item.text()
        # change the match data set
        if col == 2:
            hp.score(self.log,self.match[row+1]['index'],txt)

