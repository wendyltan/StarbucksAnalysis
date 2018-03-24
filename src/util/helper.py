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
import random
import pandas as pd
from collections import Counter


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

def check_map_range_valid(continent):
    """
    check if map_country is valid
    :param continent:
    :return:
    """
    valid_range_list = ["world", "usa", "europe", "asia", "africa", "north america", "south america"]
    if continent.lower() in valid_range_list:
        return False
    else:
        return True

def get_seperate_list(raw_result):
    """
    seperate a n-dimension list into n list with group by each item
    ex: gen_seperate_list([[1,'b'],[2,'a']]) >>> [1,2],['b','a']
    :param raw_result:
    :return:
    """

    #get raw_result's item's count
    count = Counter(raw_result[0]).__len__()
    all = Counter(raw_result).__len__()
    i=0
    j=0

    while j < count:
        new_list = []
        while i < all:
            new_list.append(raw_result[i][j])
            i+=1
        yield(new_list)
        i = 0
        j += 1


def set_random_color(dataframe,column):
    """
    用于生成原有属性对应的随机rgb值，并插入原有的DataFrame中，返回DataFrame数据
    例如set_random_color(starbucks,Timezone)，用于生成不同时区对应不同颜色
    :param dataframe:原有的DataFrame数据
    :param column:根据的列名
    :return:带有“Rgb Value”的DataFrame数据
    """
    column_color = {}
    column_color_for_df = []
    column_color_df = {}
    for column_value in dataframe[column]:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_value = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
        if column_value not in column_color.keys() and rgb_value not in column_color.values():
            column_color[column_value] = rgb_value
    for column_value in dataframe[column]:
        column_color_for_df.append(column_color[column_value])
    column_color_df["Rgb Value"] = column_color_for_df
    color_df = pd.DataFrame(column_color_df)
    dataframe.insert(len(dataframe.columns),"Rgb Value",color_df)
    return dataframe
