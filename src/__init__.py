#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 0:20
# @Author  : Wendyltanpcy
# @File    : __init__.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///starbucks.db')
Session = sessionmaker(bind=engine)