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
import time
import os
import json


if __name__ == '__main__':

    # 程序主循环
    app = br.QApplication(sys.argv)
    window = br.MainWindow()
    window.show()
    app.exec_()





