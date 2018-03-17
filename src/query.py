#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 15:23
# @Author  : Wendyltanpcy
# @File    : query.py
# @Software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///starbucks.db')
Session = sessionmaker(bind=engine)

def get_col_result(table):
    s = Session()
    # do query
    result = s.query(table).filter(table.latitude).all()
    for row in result:
        print(row.latitude)
    s.close()