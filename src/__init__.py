#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 0:20
# @Author  : Wendyltanpcy
# @File    : __init__.py
# @Software: PyCharm
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.util import excel2sql as es
from src import models as md

file_name = 'dataset/dataset.xlsx'
db_name = 'starbucks.db'

# database init
if not os.path.exists(db_name):
    # transfer excel to database
    es.doTransfer(file_name,db_name)

#data table init
table = md.Starbuck
engine = create_engine('sqlite:///starbucks.db')
Session = sessionmaker(bind=engine)