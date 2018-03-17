#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:00
# @Author  : Wendyltanpcy
# @File    : main.py
# @Software: PyCharm

import numpy as np
import os
from Code import exceltosql as es
from Code import models as md
from Code import query as qr

if __name__ == '__main__':
    file_name = 'dataset/dataset.xlsx'
    db_name = 'starbucks.db'
    if not os.path.exists(db_name):
        # transfer excel to database
        es.doTransfer(file_name,db_name)
    table = md.Starbuck
    qr.get_col_result(table)


