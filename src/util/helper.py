#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 0:09
# @Author  : Wendyltanpcy
# @File    : helper.py
# @Software: PyCharm

"""
all help functions go into here
"""

import re

def row_into_list(result):
    """
    read raw result and put it in list
    :param result:
    :return:
    """
    list = []
    for row in result:
        list.append(row)
    return  list

def check_if_valid(country_code):
    '''
    check if country_code is valid
    :param country_code:
    :return:
    '''
    pattern = re.compile('^[A-Z]{2}$')
    result = re.match(pattern, country_code)
    if result:
        return True
    else:
        return False

def get_seperate_list(raw_result):
    """
    seperate a two-dimension list into two list
    :param raw_result:
    :return:
    """
    key = []
    value = []

    for row in raw_result:
        key.append(row[0])
        value.append(row[1])
    return key,value